from django.shortcuts import render

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
    return render(request, 'plants/index.html', {
        'plants': plants
    })
