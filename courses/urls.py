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
    path('go-2/', views.Go_2, name="Go_2"),
    path('go-3/', views.Go_3, name="Go_3"),
    path('go-4/', views.Go_4, name="Go_4"),
    path('go-5/', views.Go_5, name="Go_5"),
    path('go-6/', views.Go_6, name="Go_6"),
    path('go-7/', views.Go_7, name="Go_7"),
    path('go-8/', views.Go_8, name="Go_8"),


    # Deno End Points - Mudasir Ali
    path('deno-1/', views.Deno_1, name="Deno_1"),
    path('deno-2/', views.Deno_2, name="Deno_2"),
    path('deno-3/', views.Deno_3, name="Deno_3"),

    # Ethical Hacking End Points - Mudasir Ali
    path('ethicalhacking-1/', views.EthicalHacking_1, name="EthicalHacking_1"),
    path('ethicalhacking-2/', views.EthicalHacking_2, name="EthicalHacking_2"),

    # Selenium End Points - Mudasir Ali
    path('selenium-1/', views.Selenium_1, name="Selenium_1"),
    path('selenium-2/', views.Selenium_2, name="Selenium_2"),

    

]
