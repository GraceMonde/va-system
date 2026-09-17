from django import forms
from .models import VerbalAutopsy

class VerbalAutopsyForm(forms.ModelForm):
    
    #this adds form-control to every field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        
    class Meta:
        model = VerbalAutopsy
        fields = "__all__"
        
        widgets = {
            "date_of_death": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "interview_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }