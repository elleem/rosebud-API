## Project: Django REST API with Authentication and Production Server

Author: Lauren Main

Version 1.0

### Links and Resources

Thanks to Schitt's Creek for all the fun quotes.

### Overview

Updating Django REST API, by adding Authentication and switching to a production server. 

#### Features

- [x] Add JWT Authentication to your API. 
- [x] Keep any pre-existing authentication so DRF browsable API is still usable
- [x] Switch to Gunicorn
- [x] Use Whitenoise to handle static files
- [x] Test via curl


### Setup

initiate a virtual environment

`python3.11 -m venv .venv`

`source .venv/bin/activate`

### how to initialize/run this app

`docker compose start`
`docker compose up run web python manage.py migrate`
`docker compose up run web python manage.py createsuperuser`
`docker compose up`


### tests

`python manage.py test`



