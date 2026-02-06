from django.contrib import admin
from .models import Intervention, TypeIntervention


@admin.register(TypeIntervention)

class TypeInterventionAdmin(admin.ModelAdmin):
    list_display=('id','nom')
    search_fields=('nom',)



@admin.register(Intervention)

class InterventionAdmin(admin.ModelAdmin):
     list_display = (
        'id',
        'ticket',
        'technicien',
        'date_intervention',
        'date_cloture',
        'est_termine',
        )
     list_filter = (
        'est_termine',
        'date_intervention',
        )

     search_fields = (
        'ticket__titre',
        'technicien__username',
    )