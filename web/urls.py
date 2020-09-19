"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Tech MUD Admin"
admin.site.site_title = "Tech MUD Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='Index'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('signup/', views.Signup, name="Signup"),
    path('login/', views.Login, name="Login"),
    path('logout/', views.Logout, name="Logout"),

    path('videos/', include('videos.urls')),
    path('blogs/', include('blog.urls')),
    path('courses/', include('courses.urls')),

    # Facebook Link
    path('https://www.facebook.com/techmub/', views.Facebook, name="Facebook_link"),

    # Github Link
    path('https://github.com/mudasiralinizamani', views.Github, name="Github_link"),

    #  Twiter Link
    path('https://twitter.com/Mudasir78169406', views.Twitter, name="Twitter_link"),
    
]
