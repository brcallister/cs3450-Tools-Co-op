# Startup Instructions


## Installation Instructions

1. Install Python.
2. Install Django.
3. Clone our server repository.

Our server is running through the Django framework for Python, so in order for it to work, we will need to install both of those.  Python can be installed through their official website, as outlined in this third-party tutorial:
https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html
Next, we can install Django through the command prompt.  Simply use the following command:

`pip install django`

Finally, clone this repository to the computer on which the server will be run, and you will be ready to go.

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

## Website Functionality and Usage

The website is split into three parts.

1. The customer pages.
2. The staff pages.
3. The admin pages.

The customer pages are found at `127.0.0.1:8000/Toolshop`, and consist of several unlocked information pages, as well as a password-protected account page, and password-protected reservation page.  The account page gives the customer userful information, allows them to update their account information, and actually reserve tools from the company.

The staff pages are accessed through the "Employee Portal" link, and can only be logged into by company employees.  The staff pages allow company employees to view user/tool information, check tools in, and settle fees on user accounts.

The admin page is for company owners/managers and require a staff account to log in.  The admin pages allow you to view, add to, and edit all company information stored in the database, including customer information, tool information, and messages sent through the "Contact Us" page of the website.

## Password protected content

Several pages on the website are locked by a login page, through which only a registered account can proceed.  An account has been set up for testing purposes while the website is still under development.

Username: danwatson
Password: test12345

