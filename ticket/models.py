from django.db import models
from django.conf import settings
from Parcinfo.models import Equipement

Utilisateur= settings.AUTH_USER_MODEL

class TypeDemande(models.Model):
    nom= models.CharField()
    
    def __str__(self):
        return self.nom

class Ticket(models.Model):
    STATUT_CHOIX=(
        ('ouvert','Ouvert'),
        ('en_cours','En_cours'),
        ('fermer','Fermer')
    )
    
    titre= models.CharField()
    description= models.TextField()
    utilisateur= models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    equipement= models.ForeignKey(Equipement, on_delete=models.SET_NULL, null=True)
    type_demande= models.ForeignKey(TypeDemande, on_delete=models.SET_NULL, null=True)
    statut= models.CharField(choices= STATUT_CHOIX, default='ouvert')
    date_creation= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.titre
