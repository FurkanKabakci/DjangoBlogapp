from typing import Any
from django import forms


class LoginForm(forms.Form):
    username= forms.CharField(label="Kullanici Adi:")
    password= forms.CharField(label="Parola       :", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username= forms.CharField(max_length= 50, label="Kullanici Adi:")
    password= forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm= forms.CharField(max_length=20, label="Parolayi Dogrulayiniz:", widget=forms.PasswordInput)

    def clean(self):
        username= self.cleaned_data.get("username")
        password= self.cleaned_data.get("password")
        confirm= self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar Eslesmiyor!")
        
        values= {
            "username": username,
            "password": password,   
        }