from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #path('', views.dashboard, name='dashboard'),
    path('', views.liste_tickets, name='liste_tickets'),
    path('creer/', views.creer_ticket, name='creer_ticket'),
    path('assigner/<int:pk>', views.assigner_ticket, name='assigner_ticket'),
]