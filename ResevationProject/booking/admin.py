# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from booking.models import Resource, Booking

admin.site.register(Resource)
admin.site.register(Booking)
