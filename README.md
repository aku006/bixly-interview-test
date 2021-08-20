# bixly-interview-test
This interview test program uses a terminal (I used WSL Ubuntu, but any terminal should work) and Postman. This is a simple backend that holds a garage with cars, trucks, and boats, built using the Django Rest Framework and Simple JWT for authentication. Postman is used to send HTTP requests to this backend.

## Setting Up
After cloning this repo in your terminal of choice, go inside the folder and first set up and activate the virtual environment:

    python3 -m venv env
    source env/bin/activate
    cd mysite

Once in `/mysite`, follow these commands to install the packages needed to run this app:

    pip install --upgrade pip
    pip install django
    pip install djangorestframework
    pip install djangorestframework-simplejwt

Then you need to migrate the files and create a superuser (follow the prompts for the superuser):
    
    python manage.py migrate
    python manage.py createsuperuser
    
If you haven't done so yet, install Postman at the following URL: https://www.postman.com/downloads/

## General Instructions For Testing the Server
To run this app, go to your terminal and run this command: `python3 manage.py runserver`. Open up Postman as well.

In case you have never used Postman before, in general, Postman works by sending an HTTP request to the URL in the address bar. To the left of the address bar is a dropdown menu with a list of HTTP methods, such as GET, POST, and DELETE; to the right of the address bar is a blue button, "Send," which will send the type of request you make to this URL. Right below that is a number of headers with some space below it; this is where you enter your data for the HTTP request to use. Below that is the output menu that returns to you the data from each HTTP request. You can also open multiple tabs the same way you would in a browser at the top.
