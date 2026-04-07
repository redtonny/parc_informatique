from django import forms
from .models import Intervention, TypeIntervention
from utilisateurs.models import Utilisateur

BASE_INPUT_CLASS = "border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"


class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ["ticket", "technicien", "description", "est_termine"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ne proposer que les techniciens
        self.fields["technicien"].queryset = Utilisateur.objects.filter(role="technicien")

        for name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_classes} {BASE_INPUT_CLASS}".strip()


class TypeInterventionForm(forms.ModelForm):
    class Meta:
        model = TypeIntervention
        fields = ["nom"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_classes} {BASE_INPUT_CLASS}".strip()
