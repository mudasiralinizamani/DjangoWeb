from django.urls import path
from . import views

# Create Urls for Courses - Mudasir Ali

urlpatterns = [
    path('', views.Courses, name='Courses'),

    # Nodejs End Points  - Mudasir Ali
    path('nodejs-1/', views.Nodejs_1, name="Nodejs_1"),
    path('nodejs-2/', views.Nodejs_2, name="Nodejs_2"),
    path('nodejs-3/', views.Nodejs_3, name="Nodejs_3"),
    path('nodejs-4/', views.Nodejs_4, name="Nodejs_4"),
    path('nodejs-5/', views.Nodejs_5, name="Nodejs_5"),

    # Golang End Points - Mudasir Ali
    path('go-1/', views.Go_1, name="Go_1"),

    # Deno End Points - Mudasir Ali
    path('deno-1/', views.Deno_1, name="Deno_1"),

    # Ethical Hacking End Points - Mudasir Ali
    path('ethicalhacking-1/', views.EthicalHacking_1, name="EthicalHacking_1"),

    # Selenium End Points - Mudasir Ali
    path('selenium-1/', views.Selenium_1, name="Selenium_1"),

    

]
