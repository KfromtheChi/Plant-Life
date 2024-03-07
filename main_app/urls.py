from django.urls import path
from . import views
	
urlpatterns = [
    # this root route will display the home page
    path('', views.home, name='home'),
    # this route will display the about page
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('plants/', views.plants, name='index'),
    path('care/', views.care, name='care'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
]