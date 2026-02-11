from django.db import models
from django.contrib.auth.models import AbstractUser

class Departement(models.Model):
    nom= models.CharField()
    
    def __str__(self):
        return self.nom


class Utilisateur(AbstractUser):
    ROLE_CHOIX =(
        ('utilisateur','Utilisateur'),
        ('technicien','Technicien'),
        ('admin','Administrateur'),
    )
    role= models.CharField(choices=ROLE_CHOIX, default='utilisateur')
    departement= models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return self.username