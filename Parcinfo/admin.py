from django.contrib import admin
from .models import TypeEquipement, Equipement, Etat

@admin.register(TypeEquipement)
class TypeEquipementAdmin(admin.ModelAdmin):
    list_display=('nom',)
    
@admin.register(Etat)
class EtatAdmin(admin.ModelAdmin):
    list_display=('nom',)

@admin.register(Equipement)
class Equipementadmin(admin.ModelAdmin):
    list_display=('nom','numero_serie','type_equipement', 'etat', 'date_achat','description',)
    
    search_fields=('type_equipement','numero_serie',)
    
    list_filter=('nom','etat',)