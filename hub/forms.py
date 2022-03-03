from django import forms
from .models import Student

class StudentForm(forms.Form):
    first_name =forms.CharField(
        label='Prenom',
        max_length=50
    )
    last_name =forms.CharField(
        label='Nom'
       
    )
    email =forms.EmailField()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ="__all__" #['Last_name', 'first_name','email']
        # exclude=[]
        
