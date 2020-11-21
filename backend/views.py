from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from backend.models import react360, EventTracker, FullScreen, GazeTracker, VirtualObject
from .serializers import ReactSerializer, EventSerializer, FullScreenSerializer, GazeTrackerSerializer, VirtualObjectSerializer
from .methods import csv_to_db
from .models import Purchase
from .charts import objects_to_df,Chart
from .fixation_detection import fixation_saccade_detection
from django.views.generic import TemplateView
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import plotly.graph_objects as go

from Geometry3D import *

# Create your views here.

#API View for listing the meals 
class ReactListView (ListAPIView):
    queryset = react360.objects.all()
    serializer_class = ReactSerializer

class ReactCreateView (CreateAPIView):
    queryset = react360.objects.all()
    serializer_class = ReactSerializer

class EventListView (ListAPIView):
    queryset = EventTracker.objects.all()
    serializer_class = EventSerializer

class EventCreateView (CreateAPIView):
    queryset = EventTracker.objects.all()
    serializer_class = EventSerializer
    
class FullScreenListView (ListAPIView):
    queryset = FullScreen.objects.all()
    serializer_class = FullScreenSerializer

class FullScreenCreateView (CreateAPIView):
    queryset = FullScreen.objects.all()
    serializer_class = FullScreenSerializer

class GazeTrackerListView (ListAPIView):
    queryset = GazeTracker.objects.all()
    serializer_class = GazeTrackerSerializer

class GazeTrackerCreateView (CreateAPIView):
    queryset = GazeTracker.objects.all()
    serializer_class = GazeTrackerSerializer

class VirtualObjectListView (ListAPIView):
    queryset = VirtualObject.objects.all()
    serializer_class = VirtualObjectSerializer

class VirtualObjectCreateView (CreateAPIView):
    queryset = VirtualObject.objects.all()
    serializer_class = VirtualObjectSerializer

PALETTE = ['#465b65', '#184c9c', '#d33035', '#ffc107', '#28a745', '#6f7f8c', '#6610f2', '#6e9fa5', '#fd7e14', '#e83e8c',
           '#17a2b8', '#6f42c1']

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        # get the data from th  e default method
        context = super().get_context_data(**kwargs)

        # the fields we will use
        # df_fields = ['city', 'customer_type', 'gender', 'unit_price', 'quantity',
        #     'product_line', 'tax', 'total' , 'date', 'time', 'payment',
        #     'cogs', 'profit', 'rating']

        # fields to exclude
        # df_exclude = ['id', 'cogs']

        # create a datframe with all the records.  chart.js doesn't deal well
        # with dates in all situations so our method will convert them to strings
        # however we will need to identify the date columns and the format we want.
        # I am useing just month and year here.
        df = objects_to_df(Purchase, date_cols=['%Y-%m', 'date'])

        # create a charts context to hold all of the charts
        context['charts'] = []

        ### every chart is added the same way so I will just document the first one
        # create a chart object with a unique chart_id and color palette
        # if not chart_id or color palette is provided these will be randomly generated
        # the type of charts does need to be identified here and might iffer from the chartjs type
        city_payment_radar = Chart('radar', chart_id='city_payment_radar', palette=PALETTE)
        # create a pandas pivot_table based on the fields and aggregation we want
        # stacks are used for either grouping or stacking a certain column
        city_payment_radar.from_df(df, values='total', stacks=['payment'], labels=['city'])
        # add the presentation of the chart to the charts context
        context['charts'].append(city_payment_radar.get_presentation())

        exp_polar = Chart('polarArea', chart_id='polar01', palette=PALETTE)
        exp_polar.from_df(df, values='total', labels=['payment'])
        context['charts'].append(exp_polar.get_presentation())

        exp_doughnut = Chart('doughnut', chart_id='doughnut01', palette=PALETTE)
        exp_doughnut.from_df(df, values='total', labels=['city'])
        context['charts'].append(exp_doughnut.get_presentation())

        exp_bar = Chart('bar', chart_id='bar01', palette=PALETTE)
        exp_bar.from_df(df, values='total', labels=['city'])
        context['charts'].append(exp_bar.get_presentation())

        city_payment = Chart('groupedBar', chart_id='city_payment', palette=PALETTE)
        city_payment.from_df(df, values='total', stacks=['payment'], labels=['date'])
        context['charts'].append(city_payment.get_presentation())

        city_payment_h = Chart('horizontalBar', chart_id='city_payment_h', palette=PALETTE)
        city_payment_h.from_df(df, values='total', stacks=['payment'], labels=['city'])
        context['charts'].append(city_payment_h.get_presentation())

        city_gender_h = Chart('stackedHorizontalBar', chart_id='city_gender_h', palette=PALETTE)
        city_gender_h.from_df(df, values='total', stacks=['gender'], labels=['city'])
        context['charts'].append(city_gender_h.get_presentation())

        city_gender = Chart('stackedBar', chart_id='city_gender', palette=PALETTE)
        city_gender.from_df(df, values='total', stacks=['gender'], labels=['city'])
        context['charts'].append(city_gender.get_presentation())

        gaze_df = objects_to_df(GazeTracker)

        # TODO: adjustable parameters
        gaze_df = fixation_saccade_detection(gaze_df)

        bar_chart = Chart('bar', chart_id = 'bar1', palette = PALETTE)
        bar_chart.from_df(gaze_df, values='gaze_point_z', stacks=['gaze_target'], labels='user_id', aggfunc=np.sum)
        context['charts'].append(bar_chart.get_presentation())

        bar_chart = Chart('stackedBar', chart_id='bar2', palette=PALETTE)
        bar_chart.from_df(gaze_df, values='gaze_point_z', stacks=['gaze_target'], labels='user_id', aggfunc=np.sum)
        context['charts'].append(bar_chart.get_presentation())

        doughnut = Chart('doughnut', chart_id='doughnut', palette=PALETTE)
        doughnut.from_df(gaze_df, values='gaze_point_z', labels='gaze_target', aggfunc=np.sum)
        context['charts'].append(doughnut.get_presentation())

        radar = Chart('radar', chart_id='radar', palette=PALETTE)
        radar.from_df(gaze_df, values='gaze_point_z', stacks= 'user_id', labels='gaze_target')
        context['charts'].append(radar.get_presentation())

        # Initialize figure
        fig = go.Figure()

        # y and z coordinates need to be swapped (opposite coordinate system in Unity3D)

        # add round 0 - fixations
        gaze_df_r0 = gaze_df[gaze_df['round_nr'] == '0']
        gaze_df_r0_fix = gaze_df_r0[gaze_df_r0['is_fix'] == 1]
        fig.add_trace(go.Scatter3d(x = gaze_df_r0_fix['gaze_point_x'], y = gaze_df_r0_fix['gaze_point_z'], z = gaze_df_r0_fix['gaze_point_y'], mode='markers', name='Round 0 - Fixations'))
        # add round 0 - saccades
        gaze_df_r0_sac = gaze_df_r0[gaze_df_r0['is_fix'] == 0]
        fig.add_trace(go.Scatter3d(x = gaze_df_r0_sac['gaze_point_x'], y = gaze_df_r0_sac['gaze_point_z'], z = gaze_df_r0_sac['gaze_point_y'], mode='markers', name='Round 0 - Saccades'))


        # add round 1
        gaze_df_r1 = gaze_df[gaze_df['round_nr'] == '1']
        fig.add_trace(go.Scatter3d(x = gaze_df_r1['gaze_point_x'], y = gaze_df_r1['gaze_point_z'], z = gaze_df_r1['gaze_point_y'], mode='markers', name= 'Round 1'))

        objects_df = objects_to_df(VirtualObject)
        for idx, row in objects_df.iterrows():
            # y and z coordinates need to be swapped (opposite coordinate system in Unity3D)
            verts_x = [float(i) for i in row.vertices_x.split(',')]
            verts_y = [float(i) for i in row.vertices_z.split(',')]
            verts_z = [float(i) for i in row.vertices_y.split(',')]

            fig.add_trace(go.Mesh3d(x=verts_x, y=verts_y, z=verts_z, alphahull=0, color='blue'))

        fig.update_layout(
            width=1300,
            height=700,
            updatemenus=[
                dict(
                    active=0,
                    buttons=list([
                        dict(label="All",
                             method="update",
                             args=[{"visible": [True]}]),
                        dict(label="1st round",
                             method="update",
                             args=[{"visible": [True] + [False] * 200}]),
                        dict(label="2nd round",
                             method="update",
                             args=[{"visible": [False,True] + [False] * 200}]),
                    ]),
                )
            ]
        )

        plotty = plot(fig, output_type='div', include_plotlyjs=False)

        context['fig'] = plotty

        return context