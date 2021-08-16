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

    # Returns the make, model, and year of all cars in the garage instead of the object type (ex. "Tesla Model 3 2021" instead of "Car Object (1)" will be shown)
    def __str__(self):
        return f'{self.car_make} {self.car_model} {self.car_year}'

# Truck model
class Truck(models.Model):
    # All the valus of the truck model that need to be shown
    truck_make = models.CharField(max_length=50)
    truck_model = models.CharField(max_length=50)
    truck_year = models.PositiveIntegerField(default=0)
    truck_seats = models.PositiveIntegerField(default=0)
    truck_bed_length = models.PositiveIntegerField(default=0)
    truck_color = models.CharField(max_length=50)
    truck_vin = models.CharField(max_length=17)
    truck_curr_mileage = models.PositiveIntegerField(default=0)
    truck_service_interval = models.PositiveIntegerField(default=0) # Given that service interval means number of miles before service is needed
    truck_next_service = models.DateField(default=datetime.date.today)

    # Returns the make, model, and year of all trucks in the garage instead of the object type (ex. "Ford Raptor 2018" instead of "Truck Object (1)" will be shown)
    def __str__(self):
        return f'{self.truck_make} {self.truck_model} {self.truck_year}'

# Boat model
class Boat(models.Model):
    # All the values of the boat model that need to be shown
    boat_make = models.CharField(max_length=50)
    boat_model = models.CharField(max_length=50)
    boat_year = models.PositiveIntegerField(default=0)
    boat_length = models.PositiveIntegerField(default=0)
    boat_width = models.PositiveIntegerField(default=0)
    boat_hin = models.CharField(max_length=17)
    boat_curr_hours = models.PositiveIntegerField(default=0)
    boat_service_interval = models.PositiveIntegerField(default=0) # Given that service interval means number of miles before service is needed
    boat_next_service = models.DateField(default=datetime.date.today)

    # Returns the make, model, and year of all boats in the garage instead of the object type (ex. "Tesla Model 3 2021" instead of "Boat Object (1)" will be shown)
    def __str__(self):
        return f'{self.boat_make} {self.boat_model} {self.boat_year}'