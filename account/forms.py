from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class FormularioLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistroUsuario(forms.ModelForm):
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita sua senha',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não são iguais.')
        return cd['password2']