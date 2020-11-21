from django.contrib import admin
from backend.models import react360, EventTracker, FullScreen, GazeTracker, Student, VirtualObject
from django.db.models import Count
from django.db.models.functions import TruncDay
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Purchase

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'language', 'grades', 'gender')
    list_filter = ('language', 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

class EventList(admin.ModelAdmin):
    list_display= ('timestamp', 'item', 'event')
    
class ReactList(admin.ModelAdmin):
    list_display= ('timestamp', 'x_axis', 'y_axis')
    
class FullScreenList(admin.ModelAdmin):
    list_display= ('timestamp', 'page', 'event')

class VirtualObjectAdmin(admin.ModelAdmin):
    list_display= ('vertices_x', 'vertices_y', 'vertices_z')

class GazeTrackerAdmin(admin.ModelAdmin):
    list_display= ('created_at','user_id','round_nr','subround_nr', 'gaze_target',
                   'gaze_origin_x',"gaze_origin_y","gaze_origin_z",
                   'gaze_direction_x', "gaze_direction_y", "gaze_direction_z",
                   'gaze_point_x', "gaze_point_y", "gaze_point_z",
                   )
    list_filter = ('user_id','gaze_target','created_at')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list.html'

'''
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            GazeTracker.objects.annotate(date=TruncDay("created_at"))
                .values("date")
                .annotate(y=Count("id"))
                .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
'''

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(GazeTracker, GazeTrackerAdmin)
admin.site.register(VirtualObject, VirtualObjectAdmin)
admin.site.register(Purchase)
#admin.site.register(react360, ReactList)
#admin.site.register(EventTracker, EventList)
#admin.site.register(FullScreen, FullScreenList)

