from ticket.models import Ticket
#from utilisateurs.models import Utilisateur
from interventions.models import Intervention
from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    total_tickets =  Ticket.objects.count()
    tickets_ouverts= Ticket.objects.filter(statut='ouvert').count()
    tickets_fermes= Ticket.objects.filter(statut='fermer').count()
    interventions_terminees= Intervention.objects.filter(est_termine=True).count()
    techniciens= Intervention.objects.values('technicien__username').annotate(
        total=Count('id')
    ).order_by('-total')[:5]
    
    context={
        'total_tickets':total_tickets,
        'tickets_ouverts':tickets_ouverts,
        'tickets_fermes':tickets_fermes,
        'interventions_terminees':interventions_terminees,
        'techniciens':techniciens,
    }
    
    return render(request, "registration/dashboard.html", context)

