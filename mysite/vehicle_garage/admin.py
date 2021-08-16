from django.contrib import admin
from .models import Car, Truck, Boat

# Allows user to edit vehicle listings from admin page
admin.site.register(Car)
admin.site.register(Truck)
admin.site.register(Boat)