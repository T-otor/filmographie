from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Cat(models.Model):
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=100000)

    def __str__(self):
        chaine = f"Nom {self.Nom}, Description {self.Description}"
        return chaine
    def dico(self):
        dico = {'Nom': self.Nom, 'Description': self.Description}
        return dico

class Act(models.Model):
    Nom = models.CharField(max_length=50)

    def __str__(self):
        chaine = f"Nom {self.Nom}"
        return chaine
    def dico(self):
        dico = {'Nom': self.Nom}
        return dico


class Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        chaine = f"{self.type}"
        return chaine


class Personne(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Age = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=50)
    def __str__(self):
        chaine = f"Nom {self.Nom}, Prenom {self.Prenom}, Age {self.Age}, mail {self.mail}, password {self.password}, type {self.type}, pseudo {self.pseudo}"
        return chaine   
    def dico(self):
        dico = {'Nom': self.Nom, 'Prenom': self.Prenom, 'Age': self.Age, 'mail': self.mail, 'password': self.password, 'type': self.type, 'pseudo': self.pseudo}
        return dico

class Realisateur(models.Model):
    Nom = models.CharField(max_length=50)
    def __str__(self):
        chaine = f"Nom {self.Nom}"
        return chaine
    def dico(self):
        dico = {'Nom': self.Nom}
        return dico


class Film(models.Model):
    titre = models.CharField(max_length=50)
    annee = models.DateField()
    genre = models.CharField(max_length=50)
    realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE)
    acteur_principal = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=100000)
    note = models.IntegerField()
    def __str__(self):
        chaine = f"titre {self.titre}, annee {self.annee}, genre {self.genre}, realisateur {self.realisateur}, acteur_principal {self.acteur_principal}, synopsis {self.synopsis}, note {self.note}"
        return chaine
    def dico(self):
        dico = {'titre': self.titre, 'annee': self.annee, 'genre': self.genre, 'realisateur': self.realisateur, 'acteur_principal': self.acteur_principal, 'synopsis': self.synopsis, 'note': self.note}
        return dico

