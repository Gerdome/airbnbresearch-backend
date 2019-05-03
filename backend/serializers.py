from rest_framework import serializers

from backend.models import react360


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = react360
        fields = '__all__'
        
