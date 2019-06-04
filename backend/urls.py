from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReactListView, ReactCreateView, EventCreateView, EventListView, FullScreenListView, FullScreenCreateView
from django.urls import path, include


urlpatterns = [
    path('react', ReactListView.as_view()),
    path('react/create/', ReactCreateView.as_view()),
    path('fullscreen', FullScreenListView.as_view()),
    path('fullscreen/create/', FullScreenCreateView.as_view()),
    path('event', EventListView.as_view()),
    path('event/create', EventCreateView.as_view())
]
