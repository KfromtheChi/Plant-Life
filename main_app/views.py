from django.shortcuts import render

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html') # The .html file extension renders the home page template
# Define the about view
def about(request):
    return render(request, 'about.html') # The .html file extension renders the about page template
