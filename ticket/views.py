from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from .forms import AssignationForm
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

@login_required
def creer_ticket(request):

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.utilisateur = request.user
            ticket.save()
            return redirect("liste_tickets")

    else:
        form = TicketForm()

    context = {"form": form}
    return render(request, "ticket/creation.html", context)

@login_required
def assigner_ticket(request, pk):

    ticket = Ticket.objects.get(id=pk)

    if request.method == "POST":
        form = AssignationForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect("liste_tickets")

    else:
        form = AssignationForm(instance=ticket)

    context = {
        "form": form,
        "ticket": ticket
    }

    return render(
        request,"ticket/assigner_ticket.html",context
    )
