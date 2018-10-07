# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from models import Resource, Booking 
from forms import BookingForm, UserForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    """
    Page d acceuil
    """
    resources = Resource.objects.all()
    username = request.user.username
    return render(request, 'test/home.html', {
        'resources': resources,
        'username': username
        })
# @login_required
def booking_form(request):
    """
    Creation d'un formulaire de reservation
    """
    form = BookingForm(request.POST or None)
    if form.is_valid(): 
        envoi = True
        booking = form.save(commit=False)
        booking.author = request.user.username
        booking.save()
        
    return render(request, 'booking/bookingForm.html', locals())
#                   {
#         'form': form,
#         'envoi': envoi 
#         })

def user_form(request):
    """
    """
    sauvegarde = False
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        sauvegarde = True

    return render(request, 'booking/userForm.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })
    
def connexion(request):
    """
    Page de connexion
    """
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: 
                login(request, user)  
            else: 
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'booking/connexionForm.html', locals())

def deconnexion(request):
    """
    Page de deconnexion
    """
    logout(request)
    return redirect(reverse(connexion))


