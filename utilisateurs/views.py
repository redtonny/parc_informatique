from ticket.models import Ticket
from interventions.models import Intervention
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .forms import UtilisateurCreationForm, DepartementForm


@login_required
def dashboard(request):
    total_tickets = Ticket.objects.count()
    tickets_ouverts = Ticket.objects.filter(statut='ouvert').count()
    tickets_fermes = Ticket.objects.filter(statut='ferme').count()
    interventions_terminees = Intervention.objects.filter(est_termine=True).count()
    techniciens = (
        Intervention.objects.values('technicien__username')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    # Popup / notification de bienvenue une seule fois par session
    if not request.session.get("has_seen_welcome", False):
        messages.success(request, f"Bienvenue {request.user.username} !")
        request.session["has_seen_welcome"] = True

    context = {
        'total_tickets': total_tickets,
        'tickets_ouverts': tickets_ouverts,
        'tickets_fermes': tickets_fermes,
        'interventions_terminees': interventions_terminees,
        'techniciens': techniciens,
    }

    return render(request, "registration/dashboard.html", context)


@login_required
def creer_utilisateur(request):
    # Réservé aux admins
    if not (request.user.is_superuser or getattr(request.user, "role", "").strip() == "admin"):
        messages.error(request, "Vous n'êtes pas autorisé à créer des utilisateurs.")
        return redirect("dashboard")

    if request.method == "POST":
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utilisateur créé avec succès.")
            return redirect("dashboard")
    else:
        form = UtilisateurCreationForm()

    return render(request, "utilisateurs/creer_utilisateur.html", {"form": form})


@login_required
def creer_departement(request):
    # Réservé aux admins
    if not (request.user.is_superuser or getattr(request.user, "role", "").strip() == "admin"):
        messages.error(request, "Vous n'êtes pas autorisé à créer des départements.")
        return redirect("dashboard")

    if request.method == "POST":
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Département créé avec succès.")
            return redirect("creer_utilisateur")
    else:
        form = DepartementForm()

    return render(request, "utilisateurs/creer_departement.html", {"form": form})


@csrf_exempt
@login_required
def custom_logout(request):
    """
    Déconnexion sans erreur CSRF (autorise GET/POST).
    """
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect("login")
