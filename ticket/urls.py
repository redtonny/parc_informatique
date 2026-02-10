from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path("tickets/", login_required(views.liste_tickets),nom="liste_tickets"),
]