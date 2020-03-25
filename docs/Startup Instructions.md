# Startup Instructions


## Installation Instructions

1. Install Python.
2. Install Django.
3. Clone our server repository.

Our server is running through the Django framework for Python, so in order for it to work, we will need to install both of those.  Python can be installed through their official website, as outlined in this third-party tutorial:
https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html
Next, we can install Django through the command prompt.  Simply use the following command:

`pip install django`

Finally, clone this repo to the computer on which the server will be run, and you will be ready to go.

## Running the server

In order to run the server, simply navigate to the folder that houses the file "manage.py", and run the following command in the command prompt:

`python manage.py runserver`

The server will boot up, and now be operational.  To access our site, use a web browser to navigate to

`127.0.0.1:8000/Toolshop`

for the main page, and

`127.0.0.1:8000/admin`

for the admin page.

## Running Unit Tests

In order to run our server's unit tests, once again navigate to the folder that houses the file "manage.py", and run the following command in the command prompt:

`python manage.py test Toolshop`

The unit tests will then run autonomously, reporting on their status as they go.