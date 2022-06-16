from operator import index
from django.urls import path
from django.urls import path, include # new
from . import views
urlpatterns = [
    path('index/', views.index),
    path('ajout_categorie/', views.ajout_categorie),
    path('traitement_cat/', views.traitement_cat),
    path('show_cat/', views.show_cat),
    path('delete/cat/<int:id>', views.delete_cat),
    path('modif/cat/<int:id>', views.modif_categorie),
    path('ajout_acteur/', views.ajout_acteur),
    path('traitement_act/', views.traitement_act),
    path('show_act/', views.show_act),
    path('delete/act/<int:id>', views.delete_act),
    path('modif/act/<int:id>', views.modif_act),
    path('ajout_type/', views.ajout_type),
    path('traitement_type/', views.traitement_type),
    path('show_type/', views.show_type),
    path('delete/type/<int:id>', views.delete_type),
    path('modif/type/<int:id>', views.modif_type),
    path('connexion/', views.login_user),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register", views.register_request, name="register"),
]