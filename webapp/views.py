from django.shortcuts import render
from .forms import FormCat, FormAct, FormPersonne, FormType, NewUserForm, FormFilm, FormRealisateur
from . import models
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User

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


def ajout_type(request):
    if request.method == "POST":
        form = FormType(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_type.html', {'form': form})
    else:
        form = FormType()
        return render(request, 'webapp/ajout_type.html', {'form': form})
    
def traitement_type(request):
    lform = FormType(request.POST)
    if lform.is_valid():
        Type = lform.save()
        return render(request,"webapp/index.html",{"Type" : Type})
    else:
        return render(request,"webapp/ajout_type.html",{"form": lform})

def show_type(request):
    queryset = models.Type.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_type.html",{"webapp_type" : queryset})

def delete_type(request, id):
    id = models.Type.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_type")

def modif_type(request, id):
    hdd = models.Type.objects.get(pk=id)
    form = FormType(hdd.dico())
    return render(request, 'webapp/ajout_type.html',{"form":form, "id":id})


def login_user(request):
    if request.method == 'POST':
        users = request.POST.get('mail')
        passwd = request.POST.get('password')
        user = authenticate(username=mail, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("webapp/manager/")
        else:
            return render(request,"webapp/login.html")
    else:
        return render(request,"webapp/login.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect("/webapp/index/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="webapp/register.html", context={"register_form":form})

def ajout_film(request):
    if request.method == "POST":
        form = FormFilm(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_film.html', {'form': form})
    else:
        form = FormFilm()
        return render(request, 'webapp/ajout_film.html', {'form': form})

def traitement_film(request):
    lform = FormFilm(request.POST)
    if lform.is_valid():
        Film = lform.save()
        return render(request,"webapp/index.html",{"Film" : Film})
    else:
        return render(request,"webapp/ajout_film.html",{"form": lform})

def show_film(request):
    queryset = models.Film.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_film.html",{"webapp_film" : queryset})

def delete_film(request, id):
    id = models.Film.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_film")

def modif_film(request, id):
    hdd = models.Film.objects.get(pk=id)
    form = FormFilm(hdd.dico())
    return render(request, 'webapp/ajout_film.html',{"form":form, "id":id})

def ajout_realisateur(request):
    if request.method == "POST":
        form = FormRealisateur(request)
        if form.is_valid():
            return HttpResponseRedirect("/webapp/index")
        else:
            return render(request, 'webapp/ajout_realisateur.html', {'form': form})
    else:
        form = FormRealisateur()
        return render(request, 'webapp/ajout_realisateur.html', {'form': form})

def traitement_real(request):
    lform = FormRealisateur(request.POST)
    if lform.is_valid():
        Real = lform.save()
        return render(request,"webapp/index.html",{"Real" : Real})
    else:
        return render(request,"webapp/ajout_realisateur.html",{"form": lform})

def show_real(request):
    queryset = models.Realisateur.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"webapp/show_real.html",{"webapp_realisateur" : queryset})

def delete_real(request, id):
    id = models.Realisateur.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/webapp/show_real")

def modif_real(request, id):
    hdd = models.Realisateur.objects.get(pk=id)
    form = FormRealisateur(hdd.dico())
    return render(request, 'webapp/ajout_realisateur.html',{"form":form, "id":id})