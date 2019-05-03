from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from backend.models import react360
from .serializers import ReactSerializer

# Create your views here.


#API View for listing the meals 
class ReactListView (ListAPIView):
    queryset = react360.objects.all()
    serializer_class = ReactSerializer

class ReactCreateView (CreateAPIView):
    queryset = react360.objects.all()
    serializer_class = ReactSerializer