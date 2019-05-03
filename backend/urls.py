from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReactListView, ReactCreateView, EventCreateView, EventListView
from django.urls import path, include


urlpatterns = [
    path('react', ReactListView.as_view()),
    path('react/create/', ReactCreateView.as_view()),
    path('event', EventListView.as_view()),
    path('event/create', EventCreateView.as_view())
]
