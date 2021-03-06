# bixly-interview-test
This interview test program uses a terminal (I used WSL Ubuntu, but any terminal should work) and Postman. This is a simple backend that holds a garage with cars, trucks, and boats, built using the Django Rest Framework and Simple JWT for authentication. Postman is used to send HTTP requests to this backend.

# Setting Up
Make sure that you have `python3` and `python3-venv` installed on your terminal. After cloning this repo in your terminal of choice, go inside the folder and first set up and activate the virtual environment:

    python3 -m venv env
    source env/bin/activate
    cd mysite

Once in `/mysite`, first update `pip` using `pip install --upgrade pip`. Then install the following packages using `pip`:
    
    django
    djangorestframework
    djangorestframework-simplejwt==4.4.0
    PyJWT==1.7.1

Documentation for these packages can be found here:
* Django: https://docs.djangoproject.com/en/3.2/
* Django Rest Framework: https://www.django-rest-framework.org/
* Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
* PyJWT: https://pyjwt.readthedocs.io/en/stable/

Please install the mentioned version for SimpleJWT and PyJWT as listed above. This app also ran on Django Rest Framework version 3.12.4, so check if that version was installed, and if not, run `pip install djangorestframework==3.12.4` in the terminal.

You can verify which version you are running by running `pip show <package-name>`.

Then you need to migrate the files and create a superuser (follow the prompts for the superuser):
    
    python manage.py migrate
    python manage.py createsuperuser
    
If you haven't done so yet, install Postman at the following URL: https://www.postman.com/downloads/. You can create an account for Postman if you want, or you can just skip straight ahead to the app without doing so; I didn't need an account to use Postman.

# Instructions For Testing the Server
## Authentication
To run this app, go to your terminal and run this command: `python3 manage.py runserver`. Open up Postman as well.

In case you have never used Postman before, in general, Postman works by sending an HTTP request to the URL in the address bar. To the left of the address bar is a dropdown menu with a list of HTTP methods, such as `GET`, `POST`, and `DELETE`; to the right of the address bar is a blue button, "Send," which will send the type of request you make to this URL. Right below that is a number of headers with some space below it; this is where you enter your data for the HTTP request to use. Below that is the response menu that returns to you the data from each HTTP request. You can also open multiple tabs the same way you would in a browser at the top.

First, open up a new tab in Postman and enter the address shown in the terminal into the address bar. It should say something like "http://127.0.0.1:8000/." Select `GET` from the request dropdown menu, and then hit send. You should see a message in the Response menu:

    {
        "detail": "Authentication credentials were not provided."
    }
    
You first need to get an authentication token. To do that, open up a new tab (keep this tab open!) and enter the following address in the address bar: "http://127.0.0.1:8000/api/token." (Note the lack of a slash at the end of the URL; for test purposes it seemed as though I was required to *not* include the slash at the end, so I set `APPEND_SLASH = False` in the settings. I apologize if this was not asked of me to do!)

In this tab, change the request method to `POST`, and then hit send. This will return to you the following:

    {
        "username": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }
    
To set the username and password, select the "Body" tab right below the address bar, and then select "form-data." Here, you will see a table for including Key, Value, and Description. In the Key column, enter "username" and "password", respectively, and type in the corresponding superuser information in the value menu. We will not need Description for this app.

Once you have the information you need, press "Send." This should return to you a "refresh" key and an "access" key. If you like, you can open up a text editor of your choice (I just used Notepad) and copy and paste the refresh and access keys in there; otherwise, leave this tab open. Copy the access key, and then go back to the first tab you opened up.

Back in the first tab we have open, go to the Authorization tab, and in the dropdown menu for "Type," select "Bearer Token." Then paste your access token in the space next to where it says "Token," and then after making sure the HTTP request is set to `GET`, hit send. This should now show the links to the cars, trucks, and boats, like so:

    {
        "vehicle_garage/cars": "http://127.0.0.1:8000/vehicle_garage/cars",
        "vehicle_garage/trucks": "http://127.0.0.1:8000/vehicle_garage/trucks",
        "vehicle_garage/boats": "http://127.0.0.1:8000/vehicle_garage/boats"
    }
    
This token will only last for ten minutes, however, and eventually your current token will expire. Whenever this happens, go to "http://127.0.0.1:8000/api/token/refresh" in a new tab (no slash at the end!), and send a `POST` request. Here, it will tell you that a "refresh" field is required, so go to the body tab, and enter "refresh" for your Key field and your refresh token for the Value. This will then give you a new access token; paste this new token in the tab you're working with to replace the old expired access token. You may want to leave this tab open in case you need to refresh your token again; unlike the access token, you can reuse the refresh token multiple times.

## Testing HTTP Requests (Cars)
First, go to the cars link as shown ("http://127.0.0.1:8000/vehicle_garage/cars"). This will open up a new tab for you to work with. Before you do anything:

1. Go to the Authorization tab.
2. Select "Bearer Token" on the Type dropdown menu.
3. Paste your current access token into the "Token" space.

This list should be empty by default, so we will first test out the `POST` HTTP request and create some new car models. Select `POST` from the dropdown menu, then go to the "Body" tab and select "form-data." Add the following fields to the Key column:
* car_make
* car_model
* car_year
* car_seats
* car_color
* car_vin
* car_curr_mileage
* car_service_interval
* car_next_service

Some things to note for the fields:
* `car_year`, `car_seats`, `car_curr_mileage`, and `car_service_interval` must all be positive integers
* `car_vin` must be at most 17 characters (preferably 17 exactly)
* `car_next_service` must be formatted as YYYY-MM-DD
* `car_curr_mileage` and `car_service_interval` is meant to be represented in miles

Not following the first three points will not allow you to create a new car or update an existing one. However, you are free to test that out if you wish, if you want to try running a negative test (ex. put a negative number for `car_year`, more than 17 characters for `car_vin`, or the wrong date format for `car_next_service`).

We will add three cars; these cars can be any of your choosing, so long as their values are entered correctly in the Postman data form. You can use a random VIN generator for the `car_vin` field to save some time. Fill in all of the respective fields in the Value column, and then send a `POST` request after they have been filled out. Each time you send a working `POST` request, you should get something like this in the response menu:

    {
        "id": <id number>,
        "car_make": <your car make>,
        "car_model": <your car model>,
        "car_year": <the year>,
        "car_seats": <the number of car seats>,
        "car_color": <the car color>,
        "car_vin": <the vin number>,
        "car_curr_mileage": <the number of miles driven>,
        "car_service_interval": <the interval in miles you put down>,
        "car_next_service": <the date you entered>
    }
(Everything within the angle brackets is what you explictly put down.)

The "id" value is set by the app; you don't need to touch this value ever. You should now have three cars in the garage. To test out the `GET` request and get a list of cars in the garage, simply type in "http://127.0.0.1:8000/vehicle_garage/cars" in the address bar (if it isn't already), set the HTTP request to `GET`, and send it. The response menu should return to you the three vehicles that you just created.

To test the `GET` HTTP request and read the information on a specific car, append the ID number of the car you wish to change to the address bar ("http://127.0.0.1:8000/vehicle_garage/cars/:id", where :id is the ID number associated with the car you want to single out). For this case, we'll do the third car in the list, so add that car's ID to the end of the URL (in "/:id" format; the URL at this point should be "http://127.0.0.1:8000/vehicle_garage/cars/3"). This should return to you all the information about the third car in the list.

Next we'll test the `PUT` HTTP request (and the `UPDATE` operation). Here, you should be able to change any variables you would like. For now, let's change the year and color of the third car. Once you have changed the values (make sure that they're valid!), change the HTTP request to `PUT`, and then send it. You should see in the response menu the changes that you made. For example, if your `car_color` field said "Red" before and you changed the field to "Silver," the response menu should reflect that change.

Finally, we will test the `DELETE` HTTP request and delete a car from the garage. To test that out, we'll delete the current car that we're at, which should be the third car. To do that, make sure that the URL is correct and set directly to that car's ID, then simply select `DELETE` from the HTTP request dropdown menu and send the request. If you list the cars again, you should notice that the car you deleted is gone.

And that tests all the HTTP requests required for this interview for the car garage!

## Testing the Other Vehicles
The testing process for trucks and boats is basically the exact same: go to their respective URLS (updating their access tokens as needed), create three trucks or boats, list them, get data from the second truck or boat, update the year and color, and then delete it. The fields for these vehicles are different, however.

Truck fields:
* truck_make
* truck_model
* truck_year
* truck_seats
* truck_bed_length
* truck_color
* truck_vin
* truck_curr_mileage
* truck_service_interval
* truck_next_service

Some things to note about the truck fields:
* `truck_year`, `truck_seats`, `truck_bed_length`, `truck_curr_mileage`, and `truck_service_interval` must all be positive integers
* `truck_vin` must be at most 17 characters (preferably 17 exactly)
* `truck_next_service` must be formatted as YYYY-MM-DD
* `truck_curr_mileage` and `truck_service_interval` is meant to be represented in miles
* `truck_bed_length` is meant to be represented in inches

Boat fields:
* boat_make
* boat_model
* boat_year
* boat_length
* boat_width
* boat_hin
* boat_curr_hours
* boat_service_interval
* boat_next_service

Things to note about the boat fields:
* `boat_year`, `boat_length`, `boat_width`, `boat_curr_hours`, and `boat_service_interval` must all be positive integers
* `boat_hin` should be 12 characters at the most (preferably 12 exactly)
* `boat_next_service` must be formatted as YYYY-MM-DD
* `boat_length` and `boat_width` is meant to be represented in inches
* `boat_service_interval` is meant to be represented in number of hours

Not following the first three points of either trucks or boats, as listed above, will not allow you to create a new truck or boat or update an existing one. Again, however, you can test this out for yourself if you like.

## Ending Testing
Once you have ran these tests, you can close all the tabs first (don't worry about saving them), and then close Postman. On the terminal side, run `Ctrl + C` to stop the server, then run `deactivate` in the terminal to close the virtual environment.
