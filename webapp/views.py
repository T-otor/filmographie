from django.shortcuts import render
from .forms import CategorieForm

# Create your views here.

# Ajouter 
def index(request):
    return render(request, "webapp/index.html")

def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        return render(request, "webapp/ajout.html",{"form" : form})
    else: 
        form = CategorieForm()
        return render(request, "webapp/ajout.html",{"form" : form})

#il traide de quoi ? 
def traitement(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        return render(request, "webapp/traitement",{"categorie" : categorie})
    else:
        return render(request, "webapp/ajout.html",{"form" : lform})