from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Videos, name='Videos'),
    path('input-animation-with-html-css', views.Video_1, name="Video_1"),
    path('instagram-login-automation-with-python-and-selenium', views.Video_2, name='Video_2'),
    path('this-bot-will-get-followers-for-you', views.Video_3, name='Video_3')
]