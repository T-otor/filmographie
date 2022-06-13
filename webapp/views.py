from django.shortcuts import render
from .forms import FormCategorie

# Create your views here.

# Ajouter 
def index(request):
    return render(request, "webapp/index.html")

def ajout(request):
    if request.method == "POST":
        form = FormCategorie(request)
        if form.is_valid():
            return HttpResponseRedirect("webapp/traitement_categorie")
        else:
            return render(request, 'webapp/ajout.html', {'form': form})
    else:
        form = FormCategorie()
        return render(request, 'webapp/ajout.html', {"form": form})

def traitement_categorie(request):
    lform = FormCategorie(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        return render(request, 'webapp/index',{"Categorie", categorie})
    else:
        return render(request, 'webapp/ajout.html',{"form", lform})
