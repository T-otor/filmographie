from cProfile import label
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FormCat(ModelForm):
    class Meta:
            model = models.Cat
            fields = ("Nom", "Description")
            albels = {
                "Nom" : _("Nom"),
                "Description" : _("Nom")
            }

class FormAct(ModelForm):
    class Meta:
            model = models.Act
            fields = ("Nom",)
            albels = {
                "Nom" : _("Nom"),
            }

class FormType(ModelForm):
    class Meta:
            model = models.Type
            fields = ("type",)
            albels = {
                "type" : _("type"),
            }

class FormPersonne(ModelForm):
    class Meta:
            model = models.Personne
            fields = ("mail", "password", "type", "Nom", "Prenom", "Age", "pseudo")
            albels = {
                "mail" : _("mail"),
                "password" : _("password"),
                "type" : _("type"),
                "Nom" : _("Nom"),
                "Prenom" : _("Prenom"),
                "Age" : _("Age"),
                "pseudo" : _("pseudo")
            }