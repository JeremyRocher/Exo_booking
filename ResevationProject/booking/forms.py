# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils import timezone
from models import Booking, User


class BookingForm(forms.ModelForm):
    """
    Formulaire de reservation
    """
    class Meta:
        model = Booking
        exclude = ('author',)
        #fields = '__all__'



class UserForm(forms.ModelForm):
    """
    Formulaire de creation d'utilisateur
    """
    class Meta:
        model = User
        #exclude = ('author',)
        fields = '__all__'
        
        
class ConnexionForm(forms.Form):
    """
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)        
        
        