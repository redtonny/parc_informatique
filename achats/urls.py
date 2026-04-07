from django.urls import path
from . import views


urlpatterns = [
    path("fournisseurs/", views.liste_fournisseurs, name="liste_fournisseurs"),
    path("fournisseurs/nouveau/", views.creer_fournisseur, name="creer_fournisseur"),

    path("commandes/", views.liste_commandes, name="liste_commandes"),
    path("commandes/nouvelle/", views.creer_commande, name="creer_commande"),
]