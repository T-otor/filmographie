from operator import index
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('/', views.index),
    path('ajout_categorie/', views.ajout_categorie),
    path('traitement_cat/', views.traitement_cat),
    path('show_cat/', views.show_cat),
    path('delete/cat/<int:id>', views.delete_cat),
    path('modif/cat/<int:id>', views.modif_categorie),
]