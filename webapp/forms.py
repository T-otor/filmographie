from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FormCategorie(ModelForm):
    class Meta:
        models = models.Categorie
        fields = ('Nom', 'Descriptif')
        labels = {
            'Nom' : _('Nom'),
            'Descritptif' : _('Descriptif')
        }