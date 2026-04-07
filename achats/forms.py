from django import forms
from .models import Fournisseur, Commande, LigneCommande


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ["nom", "email", "telephone", "adresse"]


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["fournisseur", "ticket", "montant_total"]


class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ["equipement", "quantite", "prix_unitaire"]

