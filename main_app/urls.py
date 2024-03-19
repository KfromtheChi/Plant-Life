from django.urls import path
from . import views
	
urlpatterns = [
    # this root route will display the home page
    path('', views.home, name='home'),
    # this route will display the about page
    path('about/', views.about, name='about'),
    path('care/', views.care, name='care'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='delete'),
    path('quiz/', views.quiz, name='quiz'),
    path('submit_quiz/', views.SubmitQuiz.as_view(), name='submit_quiz'),
]