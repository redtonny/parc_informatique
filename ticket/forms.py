from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "titre",
            "description",
            "equipement",
            "type_demande",
            "priorite",
        ]

class AssignationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["technicien", "statut"]
