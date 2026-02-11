from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', views.liste_tickets, name='liste_tickets')
    #path("tickets/", login_required(views.listetickets),name="listetickets"),
]