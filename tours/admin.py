from django.contrib import admin

from django.contrib import admin
from .models import Category, Tour, Client, Booking

admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Client)
admin.site.register(Booking)
