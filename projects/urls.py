from django.urls import path
from . import views

# Create  Urls for Projects - Mudasir Ali

urlpatterns = [
    path('', views.Projects, name='Projects'),
]