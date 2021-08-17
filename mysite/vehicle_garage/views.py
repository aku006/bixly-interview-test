# Serializers used to parse and render objects into a form that
# can work with JSON
# In this case, it converts the queryset for all vehicle objects
# and allows their information to be stored in JSON format

from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Truck, Boat
from .serializers import CarSerializer, TruckSerializer, BoatSerializer

# Displays the information from CarSerializer to the user
class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Displays the information from TruckSerializer to the user
class TruckView(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

# Displays the information from BoatSerializer to the user
class BoatView(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
