from django import forms
from .models import CustomUser

class UserRegisterForm(forms.Form):
    email = forms.CharField(max_length=255, widget=forms.TextInput)
    first_name = forms.CharField(max_length=255, widget=forms.TextInput)
    last_name = forms.CharField(max_length=255, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email sudah digunakan. Silakan gunakan email lain.')
        return email

class UserLoginForm(forms.Form):       
    email = forms.CharField(max_length=255, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
