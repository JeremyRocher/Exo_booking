# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Booking(models.Model):
    """
    """
    title = models.CharField(max_length=100, verbose_name=_("Titre"))
    author = models.CharField(max_length=100, verbose_name=_("Auteur"))
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, verbose_name=_("Ressource"))
    startDate = models.DateTimeField(default=timezone.now, verbose_name=_("Date de départ"))
    stopDate = models.DateTimeField(default=timezone.now, verbose_name=_("Date de fin"))

    def __str__(self):
        """
        Le nom de l'objet
        """
        return self.title
    
    
class Resource(models.Model):
    """
    Les ressources (salles, openspace, sieges, bureaux, ...)
    """
    name = models.CharField(max_length=100, verbose_name=_("Libellé"))
    type = models.CharField(max_length=100, verbose_name=_("Type"))
    location = models.CharField(max_length=100, verbose_name=_("Emplacement"))
    capacity = models.IntegerField(default=1, verbose_name=_("Capacité"))
    
    def __str__(self):
        """
        Le nom de l'objet
        """
        return self.name
  
class User(models.Model): 
    """
    Les utilisateurs
    """
    speudo = models.CharField(max_length=100, verbose_name=_("Speudo"))
    firstName = models.CharField(max_length=100, verbose_name=_("Prénom"))
    lastname = models.CharField(max_length=100, verbose_name=_("Nom"))
    email = models.EmailField(verbose_name=_("Email"))
    timezone = models.IntegerField(verbose_name=_("Fuseau horaire"))
    
       
    def __str__(self):
        """
        Le nom de l'objet
        """
        return self.speudo
    
    
    
    
    
    
    