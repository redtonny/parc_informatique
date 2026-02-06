from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)

class UtilisateurAdmin(UserAdmin):
    model= Utilisateur
    list_display=('username', 'email', 'is_staff', 'is_active',)