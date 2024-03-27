from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant, Plant_Care, Quiz
from .forms import Plant_CareForm

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
def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })
# Define the care view
def care_tips(request):
    return render(request, 'tips.html')
# Define the plants_detail view
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    # instantiate the Plant_CareForm to be rendered in the template
    plant_care_form = Plant_CareForm()
    return render(request, 'plants/detail.html', {
        'plant': plant, 'plant_care_form': plant_care_form
    })

# Define the Plant views Create, Update, and Delete
class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/' # Redirect to the plants index page after creating a new plant

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'botanical_name', 'notes']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/' # Redirect to the plants index page after deleting a plant

# Define the submit_quiz view
class SubmitQuiz(CreateView):
    model = Quiz
    fields = '__all__'
    success_url = '/quiz/' # Redirect to the quiz page after submitting the quiz