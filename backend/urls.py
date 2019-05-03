from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReactListView, ReactCreateView
from django.urls import path, include


urlpatterns = [
    path('', ReactListView.as_view()),
    path('create/', ReactCreateView.as_view())
]
