# -*- coding: utf-8 -*-
"""

@author: aseeliger
adjusted by: germerz

"""

import os
import numpy as np
from pathlib import Path
from ast import literal_eval as make_tuple


def detect_fixation(current_fix_center, gaze_point, origin_point, centroid_members):
    """

    Parameters
    ----------
    current_fix_center : tuple
        The current centroid of the fixation, (0,0,0) if first frame.
    gaze_point : tuple
        Spatial point of eye gaze (x,y,z).
    origin_point : tuple
        Spatial point of gaze origin (x,y,z).
    centroid_members : np array
        Array of size (n,3) containing the n members of the current fixation points.

    Returns
    -------
    updated_fixation : tuple
        New centroid of the fixation.
    is_fixation : boolean
        Indication if gaze point is fixation.
    new_centroid_members : np array
        Array of size (m,3) containing the m new members of the fixation points.

    """

    # calcualte r = distance from saptial target to location of eye gaze origin
    r = np.abs(np.linalg.norm(gaze_point - origin_point))

    # select delta = threshold of acceptable gaze point deviation delta & interpupillary distance d
    # 0.01 - 0.1
    delta = 0.04
    d = 0.067

    # calculate spatial extensions
    s_x = s_y = r * delta
    s_z = s_x * (r / d)

    # calculate yaw angle psi (rotation around the y-axis)
    # & pitch angle theta (rotation around the x-axis)
    psi = np.arctan((gaze_point[0] - origin_point[0]) / (gaze_point[2] - origin_point[2]))
    theta = -np.arctan((gaze_point[1] - origin_point[1]) / (gaze_point[2] - origin_point[2]))

    # gaze point deviations
    # TODO need np.abs?
    delta_x = gaze_point[0] - current_fix_center[0]
    delta_y = gaze_point[1] - current_fix_center[1]
    delta_z = gaze_point[2] - current_fix_center[2]

    # rotate deviations
    delta_x_r = delta_x * np.cos(psi) + delta_z * np.sin(psi)
    delta_y_r = delta_y * np.cos(theta) + delta_z * np.sin(theta)
    delta_z_r = delta_z * np.cos(theta) * np.cos(psi) - delta_x * np.sin(psi) - delta_y * np.sin(theta)

    # comapre gaze_point coordiantes with bounding volume of ellipsoid
    # TODO Attention: In Paper authors use r_x, r_y, and r_z
    is_fixation = ((delta_x_r / s_x) ** 2 + (delta_y_r / s_y) ** 2 + (delta_z_r / s_z) ** 2) < 1

    # calculate new ellipsoid parameters
    if is_fixation:
        # new fixation center is center of current fixation points
        new_centroid_members = np.append(centroid_members, gaze_point).reshape(-1, 3)
        updated_fixation = centroid(new_centroid_members)
    else:
        # new fixation is current gaze point
        new_centroid_members = np.empty((0, 3))
        updated_fixation = gaze_point

    return updated_fixation, is_fixation, new_centroid_members


def detect_dwell(past_target, current_target, dwell_ctr, had_fix):
    is_dwell = False
    if (past_target != current_target):
        dwell_ctr += 1
    if had_fix:
        is_dwell = True
    return is_dwell, dwell_ctr, current_target


def centroid(arr):
    length, dim = arr.shape
    return np.array([np.sum(arr[:, i]) / length for i in range(dim)])

def fixation_saccade_detection(df):
    df = df
    n_rows = len(df)
    gazepoints = df[['gaze_point_x', 'gaze_point_y', 'gaze_point_z']]
    gazeorigins = df[['gaze_origin_x', 'gaze_origin_y', 'gaze_origin_z']]
    targets = df[['gaze_target']]

    gaze_points = gazepoints.to_numpy()
    gaze_origins = gazeorigins.to_numpy()
    eval_targets = targets.to_numpy()

    # initialize gaze protocol
    fixation_center = gaze_points[0]
    fixations = np.zeros((n_rows, 5))

    # analyze gaze protocol
    t, fix_nr, fix_length, = 0, 0, 0
    dwell_nr, dwell_length = 1, 1
    fix_length = 1
    bf, had_fix, prior = False, False, False
    centroid_members = np.empty((0, 3))
    aoi_target = "None"

    # extract fixations, saccades, and dwells from gaze points and origins
    for i in range(0, len(gaze_origins)):
        # fixation or saccade
        new_fix_center, is_fix, centroid_members = detect_fixation(fixation_center, gaze_points[i], gaze_origins[i],
                                                                   centroid_members)
        fixations[t][0] = is_fix

        if (is_fix & (not (bf))):
            fix_nr += 1
            fix_length = 1
            bf = True
        elif (not (is_fix)):
            bf = False
        if (is_fix):
            fixations[t][1] = fix_nr
            fixations[t][2] = fix_length

        fixation_center = new_fix_center
        fix_length += 1

        # dwell
        if (aoi_target != eval_targets[i]):
            # if prior gaze points contained no fixation in AOI
            if not had_fix:
                dwell_nr -= 1
            had_fix = False
            dwell_length = 1
        if not had_fix:
            had_fix = is_fix
        is_dwell, dwell_nr, aoi_target = detect_dwell(aoi_target, eval_targets[i], dwell_nr, had_fix)
        if is_dwell:
            fixations[t][3] = dwell_nr
            fixations[t][4] = dwell_length
            dwell_length += 1
        else:
            fixations[t][3] = 0

        t += 1

    print(len(fixations[:,0]), len(df))

    # include information in original dataset
    df['is_fix'] = fixations[:,0]

    del i, new_fix_center, is_fix

    # evaluate results: comapre number of looked at targets to number of fixations detected
    nr_targets = np.sum(eval_targets[:-1] != eval_targets[1:]) + 1
    nr_fixations = np.max(fixations[:, 1])

    print("Detected {} fixations from {} Unity targets".format(nr_fixations, nr_targets))

    return df