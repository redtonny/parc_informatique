from django.db import models

class TypeEquipement(models.Model):
    nom= models.CharField()
    
    def __str__(self):
        return self.nom
    
class Etat(models.Model):
    nom= models.CharField()
    
    def __str__(self):
        return self.nom
    
class Equipement(models.Model):
    nom= models.CharField()
    numero_serie= models.CharField()
    type_equipement= models.ForeignKey(TypeEquipement, on_delete=models.CASCADE)
    etat= models.ForeignKey(Etat, on_delete=models.SET_NULL, null=True)
    date_achat= models.DateField(null=True, blank=True)
    description= models.CharField()
    
    def __str__(self):
        return f"{self.nom} ({self.numero_serie})"