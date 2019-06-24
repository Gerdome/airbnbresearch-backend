from django.contrib import admin
from backend.models import react360, EventTracker, FullScreen

class EventList(admin.ModelAdmin):
    list_display= ('timestamp', 'item', 'event')
    
class ReactList(admin.ModelAdmin):
    list_display= ('timestamp', 'x_axis', 'y_axis')
    
class FullScreenList(admin.ModelAdmin):
    list_display= ('timestamp', 'page', 'event')
    

# Register your models here.
admin.site.register(react360, ReactList)
admin.site.register(EventTracker, EventList)
admin.site.register(FullScreen, FullScreenList)

