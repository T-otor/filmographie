from django.shortcuts import render
from .forms import FormCat, FormAct, FormPersonne
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
        return render(request,"webapp/ajout_categorie.html",{"form": lform})

        
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
    return render(request, 'webapp/ajout_categorie.html',{"form":form, "id":id})

def traitement_act(request):
    lform = FormAct(request.POST)
    if lform.is_valid():
        Act = lform.save()
        return render(request,"webapp/index.html",{"Act" : Act})
    else:
        return render(request,"webapp/ajout_categorie.html",{"form": lform})

    
def show_act(request):
    queryset = models.Act.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_act.html",{"webapp_act" : queryset})

def delete_act(request, id):
    id = models.Act.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_act")

def modif_act(request, id):
    hdd = models.Act.objects.get(pk=id)
    form = FormAct(hdd.dico())
    return render(request, 'webapp/ajout_acteur.html',{"form":form, "id":id})


def show_personne(request):
    queryset = models.Personne.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_personne.html",{"webapp_personne" : queryset})

def delete_personne(request, id):
    id = models.Personne.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_personne")

def modif_personne(request, id):
    hdd = models.Personne.objects.get(pk=id)
    form = FormPersonne(hdd.dico())
    return render(request, 'webapp/ajout_personne.html',{"form":form, "id":id})

def ajout_personne(request):
    if request.method == "POST":
        form = FormPersonne(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_personne.html', {'form': form})
    else:
        form = FormPersonne()
        return render(request, 'webapp/ajout_personne.html', {'form': form})
