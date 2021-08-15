from django.contrib import admin
from .models import Car

# Allows user to see Car listing from admin page
admin.site.register(Car)
