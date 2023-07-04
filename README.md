## Project: Django REST Framework and Docker

Author: Lauren Main

Version 1.0

### Links and Resources



### Overview

Updating Django REST  API, by adding Permissions and Postgresql Database. 

#### Features

- [x] Make your site a DRF powered API
- [x] Adjust so that authenticated users only have access to the API
- [x] Add a customer permission so that only authenticated users can update or delete
- [x] Add ability to switch users directly from browsable API


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



