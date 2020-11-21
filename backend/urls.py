from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReactListView, ReactCreateView, EventCreateView, EventListView, FullScreenListView, FullScreenCreateView, GazeTrackerListView, GazeTrackerCreateView, VirtualObjectListView, VirtualObjectCreateView
from django.urls import path, include
from backend import views

urlpatterns = [
    path('react', ReactListView.as_view()),
    path('react/create/', ReactCreateView.as_view()),
    path('fullscreen', FullScreenListView.as_view()),
    path('fullscreen/create/', FullScreenCreateView.as_view()),
    path('event', EventListView.as_view()),
    path('event/create', EventCreateView.as_view()),
    path('gazetracker', GazeTrackerListView.as_view()),
    path('gazetracker/create', GazeTrackerCreateView.as_view()),
    path('virtualobject', VirtualObjectListView.as_view()),
    path('virtualobject/create', VirtualObjectCreateView.as_view()),
    path('', views.Dashboard.as_view(), name='dashboard')
]
