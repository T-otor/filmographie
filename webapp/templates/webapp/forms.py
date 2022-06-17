from cProfile import label
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class FormFilm(ModelForm):
    class Meta:
        model = models.Film
        fields = ("titre", "annee", "genre", "realisateur", "acteur_principal", "synopsis", "note")
        labels = {
            "titre" : _("titre"),
            "annee" : _("annee"),
            "genre" : _("genre"),
            "realisateur" : _("realisateur"),
            "acteur_principal" : _("acteur_principal"),
            "synopsis" : _("synopsis"),
            "note" : _("note"),
        }