from django.shortcuts import render
from .forms import FormCategorie

# Create your views here.

# Ajouter 
def index(request):
    return render(request, "webapp/index.html")

def ajout(request):
    if request.method == "POST":
        form = FormCategorie(request)
        if form.is_valid(): # validation du formulaire.
            marque = form.save() # sauvegarde dans la base
            return render(request,"webapp/index.html",{"Marque" : marque}) #

        else:
            return render(request,"webapp/ajout.html",{"form": form})
    else :
        form = FormCategorie(request) # création d'un formulaire vide
        return render(request,"wbapp/ajoutmarque.html",{"form" : form})

def traitement_categorie(request):
    lform = FormCategorie(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        return render(request,"webapp/index.html",{"categorie" : categorie})
    else:
        return render(request,"webapp/ajout.html",{"form": lform})