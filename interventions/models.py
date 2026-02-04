from django.db import models
from django.conf import settings
from ticket.models import Ticket

Utilisateur = settings.AUTH_USER_MODEL

class Intervention(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_intervention = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Intervention - {self.ticket}"

