from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Intervention, TypeIntervention
from .forms import InterventionForm, TypeInterventionForm


@login_required
def liste_interventions(request):
    # Un admin voit tout, un technicien voit ses interventions, un utilisateur voit celles liées à ses tickets
    qs = Intervention.objects.select_related("ticket", "technicien")
    role = getattr(request.user, "role", "").strip()

    if role == "technicien":
        qs = qs.filter(technicien=request.user)
    elif role == "utilisateur":
        qs = qs.filter(ticket__utilisateur=request.user)

    context = {"interventions": qs}
    return render(request, "interventions/liste_interventions.html", context)


@login_required
def creer_intervention(request):
    # Seuls techniciens ou admins peuvent créer une intervention
    role = getattr(request.user, "role", "").strip()
    if role not in ("technicien", "admin"):
        raise PermissionDenied("Vous n'êtes pas autorisé à créer des interventions.")

    if request.method == "POST":
        form = InterventionForm(request.POST)
        if form.is_valid():
            intervention = form.save(commit=False)
            if role == "technicien" and intervention.technicien is None:
                intervention.technicien = request.user
            intervention.save()
            messages.success(request, "Intervention créée avec succès.")
            return redirect("liste_interventions")
    else:
        form = InterventionForm()
    return render(request, "interventions/form_intervention.html", {"form": form})


@login_required
def editer_intervention(request, pk):
    intervention = get_object_or_404(Intervention, pk=pk)

    role = getattr(request.user, "role", "").strip()
    if role not in ("technicien", "admin"):
        raise PermissionDenied("Vous n'êtes pas autorisé à modifier des interventions.")

    if request.method == "POST":
        form = InterventionForm(request.POST, instance=intervention)
        if form.is_valid():
            form.save()
            messages.success(request, "Intervention mise à jour avec succès.")
            return redirect("liste_interventions")
    else:
        form = InterventionForm(instance=intervention)
    return render(
        request,
        "interventions/form_intervention.html",
        {"form": form, "intervention": intervention},
    )


@login_required
def creer_type_intervention(request):
    # réservé aux admins
    role = getattr(request.user, "role", "").strip()
    if role not in ("technicien", "admin"):
        raise PermissionDenied("Vous n'êtes pas autorisé à créer des types d'intervention.")

    if request.method == "POST":
        form = TypeInterventionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Type d'intervention créé avec succès.")
            return redirect("creer_intervention")
    else:
        form = TypeInterventionForm()
    return render(request, "interventions/form_type_intervention.html", {"form": form})
