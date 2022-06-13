from django.db import models

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