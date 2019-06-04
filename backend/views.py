from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from backend.models import react360, EventTracker, FullScreen
from .serializers import ReactSerializer, EventSerializer, FullScreenSerializer

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
    queryset = EventTracker.objects.all()
    serializer_class = FullScreenSerializer