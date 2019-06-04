from rest_framework import serializers

from backend.models import react360, EventTracker, FullScreen


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
        
        
