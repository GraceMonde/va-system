from django import forms
from .models import VerbalAutopsy

class VerbalAutopsyForm(forms.ModelForm):
    class Meta:
        model = VerbalAutopsy
        fields = "__all__"
        widgets = {
            "date_of_death": forms.DateInput(
                attrs={"type": "date"}
            ),
            "interview_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }