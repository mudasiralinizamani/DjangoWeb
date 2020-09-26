from django.urls import path
from . import views


urlpatterns = [
    path('', views.Blogs, name='Blogs'),
    path('7-best-free-alternatives-of-adobe-premiere-pro/', views.Post_1, name='7_best_free_alternatives_of_adobe_premiere_pro'),
    path('6-most-popular-javascript-libraries-in-2020/', views.Post_2, name='6_most_popular_javascript_libraries_in_2020'),
    path('7-skills-you-need-as-a-javascript-developer-in-2020/', views.Post_3, name='7_skills_you_need_as_a_javascript_developer_in_2020'),
    path('top-4-dying-programming-languages-in-2020/', views.Post_4, name='top_4_dying_programming_languages_in_2020'),
    path('top-5-website-builder-apps-2020-september/', views.Post_5, name='top_5_website_builder_apps_2020_september')
    
]