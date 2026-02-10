from django.db import models
from django.conf import settings
from Parcinfo.models import Equipement
from interventions.models import TypeIntervention

Utilisateur= settings.AUTH_USER_MODEL

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
    type_demande= models.ForeignKey(TypeIntervention, on_delete=models.SET_NULL, null=True)
    statut= models.CharField(choices= STATUT_CHOIX, default='ouvert')
    date_creation= models.DateTimeField(auto_now_add=True)
    technicien= models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets_assignes", limit_choices_to={'role':'technicien'})
    departement= models.CharField(max_length=300)
    
    def __str__(self):
        return self.titre
