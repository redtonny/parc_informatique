from django.db import models
from django.conf import settings
from Parcinfo.models import Equipement
from interventions.models import TypeIntervention

Utilisateur= settings.AUTH_USER_MODEL

class Ticket(models.Model):
    STATUT_CHOIX=(
        ('ouvert','Ouvert'),
        ('en_cours','En_cours'),
        ('ferme','Fermé')
    )
    
    PRIORITE_CHOIX=(
        ("basse", "Basse"),
        ("moyenne", "Moyenne"),
        ("haute", "Haute"),
        ("critique", "Critique"),
    )
    titre= models.CharField(max_length=200)
    description= models.TextField()
    utilisateur= models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    equipement= models.ForeignKey(Equipement, on_delete=models.SET_NULL, null=True)
    priorite= models.CharField(max_length=20, choices=PRIORITE_CHOIX, default="moyenne")
    type_demande= models.ForeignKey(TypeIntervention, on_delete=models.SET_NULL, null=True)
    statut= models.CharField(max_length=25,choices= STATUT_CHOIX, default='ouvert')
    date_creation= models.DateTimeField(auto_now_add=True)
    technicien= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets_assignes")
    departement= models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.titre
