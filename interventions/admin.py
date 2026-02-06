from django.contrib import admin
from .models import Intervention

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