from django.urls import path
from . import views

# Create  Urls for Projects - Mudasir Ali

urlpatterns = [
    path('', views.Projects, name='Projects'),
    path('post-repo/', views.Post_repo, name='Post_Repo'),
]