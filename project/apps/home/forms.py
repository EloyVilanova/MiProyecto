from django import forms
from . import models

class FamiliarForms(forms.ModelForm): 
    
    class Meta: 

        models = models.Familiar

        fields = "__all__" 

