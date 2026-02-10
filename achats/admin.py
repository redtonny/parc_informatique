from django.contrib import admin
from .models import Fournisseur, Commande, LigneCommande


class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fournisseur',
        'date_commande',
        'montant_total',
    )

    inlines = [LigneCommandeInline]


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'email',
        'telephone',
    )

