from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('utilisateurs/nouveau/', views.creer_utilisateur, name='creer_utilisateur'),
    path('departements/nouveau/', views.creer_departement, name='creer_departement'),
    path('logout/', views.custom_logout, name='custom_logout'),
]