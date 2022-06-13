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
            model = models.Cat
            fields = ("Nom",)
            albels = {
                "Nom" : _("Nom"),
            }