from django.db import models
import datetime

# Car model
class Car(models.Model):
    # All the values of the car model that need to be shown
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.PositiveIntegerField(default=0)
    car_seats = models.PositiveIntegerField(default=0)
    car_color = models.CharField(max_length=50)
    car_vin = models.CharField(max_length=17)
    car_curr_mileage = models.PositiveIntegerField(default=0)
    car_service_interval = models.PositiveIntegerField(default=0) # Given that service interval means number of miles before service is needed
    car_next_service = models.DateField(default=datetime.date.today)

    # Returns the names of the cars in the garage instead of the object type (ex. "Tesla Model 3" instead of "Car Object (1)" will be shown)
    def __str__(self):
        return f'{self.car_make} {self.car_model} {self.car_year}'
