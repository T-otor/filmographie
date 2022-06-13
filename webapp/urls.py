from operator import index
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('ajout_categorie/<int:id>', views.ajout),
    path('traitement_categorie/', views.traitement_categorie),
]