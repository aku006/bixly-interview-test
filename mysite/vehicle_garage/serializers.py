# Serializers used to parse and render objects into a form that can work with JSON
# In this case, it converts the queryset for all vehicle objects
# and allows their information to be stored in JSON format
from rest_framework import serializers
from .models import Car, Truck, Boat

# Serializer for car
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('__all__')

# Serializer for truck
class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('__all__')

# Serializer for boat
class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ('__all__')