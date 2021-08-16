# Needed to translate HTTP requests to JSON
# Gives relevant info of the model to the user
# Also allows user to create and update new models
from rest_framework import serializers
from .models import Car, Truck, Boat

# Serializer for car
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id',
                'car_make',
                'car_model',
                'car_year',
                'car_seats',
                'car_color',
                'car_vin',
                'car_curr_mileage',
                'car_service_interval',
                'car_next_service')

# Serializer for truck
class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id',
                'truck_make',
                'truck_model',
                'truck_year',
                'truck_seats',
                'truck_bed_length',
                'truck_color',
                'truck_vin',
                'truck_curr_mileage',
                'truck_service_interval',
                'truck_next_service')

# Serializer for boat
class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ('id',
                'boat_make',
                'boat_model',
                'boat_year',
                'boat_length',
                'boat_width',
                'boat_hin',
                'boat_curr_hours',
                'boat_service_interval',
                'boat_next_service')