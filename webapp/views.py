from django.shortcuts import render
from .forms import FormCat
from . import models
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

def ajout_categorie(request):
    if request.method == "POST":
        form = FormCat(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_categorie.html', {'form': form})
    else:
        form = FormCat()
        return render(request, 'webapp/ajout_categorie.html', {'form': form})

def ajout_acteur(request):
    if request.method == "POST":
        form = FormAct(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_acteur.html', {'form': form})
    else:
        form = FormAct()
        return render(request, 'webapp/ajout_acteur.html', {'form': form})

def traitement_cat(request):
    lform = FormCat(request.POST)
    if lform.is_valid():
        ram = lform.save()
        return render(request,"webapp/index.html",{"Ram" : ram})
    else:
        return render(request,"webapp/ajout_categorie.htmll",{"form": lform})

        
def show_cat(request):
    queryset = models.Cat.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_cat.html",{"webapp_cat" : queryset})

def delete_cat(request, id):
    id = models.Cat.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_cat")

def modif_categorie(request, id):
    hdd = models.Cat.objects.get(pk=id)
    form = FormCat(hdd.dico())
    return render(request, 'webapt/ajout_categorie.html',{"form":form, "id":id})