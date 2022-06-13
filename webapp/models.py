from django.db import models

# Create your models here.

class categorie(models.Model):
    Nom = models.CharField(max_length=100)
    Descriptif = models.CharField(max_length=10000)

    def __str__(self):
        chaine = f"Nom {self.Nom}, Descriptif {self.Descriptif}"
        return chaine