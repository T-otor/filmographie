from django.shortcuts import render
#from .forms import FormCategorie

# Create your views here.

# Ajouter 
def index(request):
    return render(request, "webapp/index.html")
