from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from .forms import AssignationForm
from utilisateurs.models import Utilisateur
from interventions.models import Intervention
from django.db.models import Count, Q
from django.core.exceptions import PermissionDenied
from django.contrib import messages


@login_required
def liste_tickets(request):
    utilisateur = request.user

    # Utiliser .strip() et comparer avec les valeurs EXACTES
    if utilisateur.role and utilisateur.role.strip() == "admin":
        tickets = Ticket.objects.all()    
    elif utilisateur.role and utilisateur.role.strip() == "technicien":
        # Un technicien voit :
        # - Les tickets qui lui sont assignés
        # - OU les tickets non assignés (null)
        tickets = Ticket.objects.filter(
            Q(technicien=utilisateur) | 
            Q(technicien__isnull=True)
        ).distinct()   
    else:  # utilisateur normal
        tickets = Ticket.objects.filter(utilisateur=utilisateur)

    context = {"tickets": tickets}
    return render(request, "ticket/liste.html", context)


@login_required
def creer_ticket(request):

    if request.method == "POST":
        form = TicketForm(request.POST, utilisateur=request.user)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.utilisateur = request.user
            # Logique métier : rattacher le département automatiquement
            departement = getattr(request.user, "departement", None)
            if departement:
                ticket.departement = departement.nom
            # Toujours commencer au statut "ouvert"
            ticket.statut = "ouvert"
            ticket.save()
            messages.success(request, "Ticket créé avec succès.")
            return redirect("liste_tickets")

    else:
        form = TicketForm(utilisateur=request.user)

    context = {"form": form}
    return render(request, "ticket/creation.html", context)

@login_required
def assigner_ticket(request, pk):

    ticket = get_object_or_404(Ticket, id=pk)

    # Seuls les techniciens ou admins peuvent assigner un ticket
    role = getattr(request.user, "role", "").strip()
    if role not in ("technicien", "admin"):
        raise PermissionDenied("Vous n'êtes pas autorisé à assigner des tickets.")

    if request.method == "POST":
        form = AssignationForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            messages.success(request, "Ticket assigné / mis à jour avec succès.")
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
