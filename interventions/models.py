from django.db import models
from django.conf import settings
from django.utils import timezone


Utilisateur = settings.AUTH_USER_MODEL

class TypeIntervention(models.Model):
    nom= models.CharField()
    
    def __str__(self):
        return self.nom

class Intervention(models.Model):
    ticket = models.OneToOneField('ticket.Ticket', on_delete=models.CASCADE)
    technicien = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_intervention = models.DateTimeField(auto_now_add=True)
    date_cloture= models.DateTimeField(null= True, blank=True)
    est_termine= models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        creation = self.pk is None

        # Si création → ticket en cours
        if creation:
            self.ticket.statut = 'en_cours'
            self.ticket.save()

        # Si intervention terminée ET pas encore de date clôture
        if self.est_termine and not self.date_cloture:
            # Doit correspondre exactement au choix "ferme" du modèle Ticket
            self.ticket.statut = 'ferme'
            self.ticket.save()
            self.date_cloture = timezone.now()

        super().save(*args, **kwargs)

        
    def __str__(self):
        return f"Intervention #{self.pk} - {self.ticket.titre}"
    
    

