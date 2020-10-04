from django.urls import path
from . import views

# Create the Accounts Urls - Mudasir ALi

urlpatterns = [
   path('', views.Signup, name="Signup"),
   path('login/', views.Login, name="Login"),
   path('logout/', views.Logout, name="Logout"),
   path('profile/', views.Profile, name="Profile")
]