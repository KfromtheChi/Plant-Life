from django.urls import path
from . import views
	
urlpatterns = [
    # this root route will display the home page
    path('', views.home, name='home'),
]