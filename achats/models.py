from django.db import models
from ticket.models import Ticket
from Parcinfo.models import Equipement


class Fournisseur(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    fournisseur = models.ForeignKey(
        Fournisseur,
        on_delete=models.CASCADE,
        related_name="commandes"
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_commande = models.DateField(auto_now_add=True)
    montant_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Commande #{self.pk} - {self.fournisseur.nom}"
    


class LigneCommande(models.Model):
    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name="lignes"
    )
    equipement = models.ForeignKey(
        Equipement,
        on_delete=models.CASCADE
    )
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    def total_ligne(self):
        return self.quantite * self.prix_unitaire

    def __str__(self):
        return f"{self.equipement} x{self.quantite}"
