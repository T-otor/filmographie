from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategorieForm(ModelForm):
        class Meta :
            model = models.Categorie
            fields = ('id', 'nom', 'descriptif')
            labels = {
                'id' : _('ID'),
                'nom' : _('Nom'),
                'descriptif' : _('Descriptif')
            }