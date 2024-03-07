from django.urls import path
from . import views
	
urlpatterns = [
    # this root route will display the home page
    path('', views.home, name='home'),
    # this route will display the about page
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='plants')
]