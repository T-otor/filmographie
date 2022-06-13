from django.db import models

# Create your models here.

class Categorie(models.Model):
    Nom = models.CharField(max_length=100)
    Descriptif = models.CharField(max_length=1000)
    def _str_(self):
        chaine = f"{self.Nom}, {self.Descriptif}"
        return chaine