from django import forms
from .models import Genero  

class GeneroForm(forms.ModelForm): 
    class Meta:
        model = Genero  
        fields = ["genero"]
        labels = {'genero': 'Género'}
