from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FormCategorie(ModelForm):
    class Meta:
        model = models.categorie
        fields = ("Nom", "Descriptif")
        labels = {
            "Nom" : _("Nom"),
            "Descriptif" : _("Descriptif")
        }