from django.contrib import admin
from .models import Ticket, TypeDemande
from interventions.models import Intervention

@admin.register(TypeDemande)

class TypeDemandeAdmin(admin.ModelAdmin):
    list_display=('id','nom')
    search_fields=('nom',)


class InterventionInLine(admin.StackedInline):
    model= Intervention
    extra= 0
    
    
@admin.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
    inlines=[InterventionInLine]
    
    list_display=(
        'id',
        'titre',
        'utilisateur',
        'equipement',
        'type_demande',
        'statut',
        'date_creation',
    )
    
    search_fields= (
        'titre',
        'description',
        'utilisateur_username',
    )

    list_filter = (
    'statut',
    'type_demande',
    'date_creation',
    )
    ordering= ('-date_creation',)
    
    list_per_page=20

    list_editable=('statut',)
    
