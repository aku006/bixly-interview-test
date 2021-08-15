# Needed to translate HTTP requests to JSON

from rest_framework import serializers
from .models import Car

# Serializer for car
# Gives relevant info of the model to the user
# Also allows user to create and update new Car models
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
