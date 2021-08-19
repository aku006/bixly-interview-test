from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Car, Truck, Boat
from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from rest_framework.permissions import IsAuthenticated

# Opted for using viewsets classes instead of APIView for HTTP requests

# Displays the information from CarSerializer to the user
class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

# Displays the information from TruckSerializer to the user
class TruckView(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = (IsAuthenticated,)

# Displays the information from BoatSerializer to the user
class BoatView(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
    permission_classes = (IsAuthenticated,)
