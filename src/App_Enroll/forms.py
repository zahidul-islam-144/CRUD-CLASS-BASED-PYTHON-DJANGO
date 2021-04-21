from django.core import validators
from django import forms
from . models import User

class Student_Rgistration(forms.ModelForm):
    # name = forms.CharField(max_length=50, required=False) # here i can also write validators 

    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write your name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'abc@def.com'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control','placeholder':'Set password'}),
        }
