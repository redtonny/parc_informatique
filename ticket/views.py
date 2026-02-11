from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket
from utilisateurs.models import Utilisateur
from interventions.models import Intervention
from django.db.models import Count


@login_required
def liste_tickets(request):
    
    utilisateur = request.user
    
    if utilisateur.role == "admin":
        tickets= Ticket.objects.all()
    elif utilisateur.role =="technicien":
        tickets= Ticket.objects.filter(technicien=utilisateur) #departement=user.departement
    else:
        tickets= Ticket.objects.filter(utilisateur=utilisateur)
    
    context={"ticket":tickets}
    return render(request, "ticket/liste.html", context)
    