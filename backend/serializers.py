from rest_framework import serializers

from backend.models import react360, EventTracker, FullScreen, GazeTracker, VirtualObject


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = react360
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTracker
        fields = '__all__'
        
class FullScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullScreen
        fields = '__all__'

class GazeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GazeTracker
        fields = '__all__'

class VirtualObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualObject
        fields = '__all__'
        
        
