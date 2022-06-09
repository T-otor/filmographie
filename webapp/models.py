from django.db import models

# Create your models here.

class Categorie(models.Model):
    id = models.IntegerField(primary_key=True, blank= False)
    nom = models.CharField(max_length= 100)
    descriptif = models.TextField(null = True, blank= True)

    def __str__(self):
        chaine = f"{self.id} , {self.nom} , {self.descriptif}"
        return chaine
