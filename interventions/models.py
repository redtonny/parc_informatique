from django.db import models
from django.conf import settings
from ticket.models import Ticket
from django.utils import timezone
Utilisateur = settings.AUTH_USER_MODEL

class Intervention(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_intervention = models.DateTimeField(auto_now_add=True)
    date_cloture= models.DateTimeField(null= True, blank=True)
    est_termine= models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.ticket.statut='en_cours'
            self.ticket.save()
    
        if self.est_terminee:
            self.ticket.statut = 'fermer'
            self.ticket.save()
            self.date_cloture = timezone.now()

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Intervention #{self.pk} - {self.ticket.titre}"
    
    

