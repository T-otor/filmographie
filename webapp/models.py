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


class Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        chaine = f"type {self.type}"
        return chaine


class Personne(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Age = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        chaine = f"Nom {self.Nom}, Prenom {self.Prenom}, Age {self.Age}, mail {self.mail}, password {self.password}, type {self.type}"
        return chaine
    def dico(self):
        dico = {'Nom': self.Nom, 'Prenom': self.Prenom, 'Age': self.Age, 'mail': self.mail, 'password': self.password, 'type': self.type}
        return dico
        

