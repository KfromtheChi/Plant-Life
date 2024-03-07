from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Plant, Quiz

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html') # The .html file extension renders the home page template
# Define the about view
def about(request):
    return render(request, 'about.html')
# Define the quiz view
def quiz(request):
    return render(request, 'quiz/quiz.html', {
        'quiz': quiz
    })
# Define the plants view
def plants(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })
# Define the care view
def care(request):
    return render(request, 'care.html')
# Define the plants_detail view
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {
        'plant': plant
    })

# Define the PlantCreate view
class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/' # Redirect to the plants index page after creating a new plant

# Define the submit_quiz view
class SubmitQuiz(CreateView):
    model = Quiz
    fields = '__all__'
    success_url = '/quiz/' # Redirect to the quiz page after submitting the quiz