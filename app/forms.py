from django.forms import ModelForm
from .models import student
from django import forms

class studentForm(ModelForm):

    class Meta:
        model = student
        fields = '__all__'



        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})

        }