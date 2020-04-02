# Django-country-utils

Package to add Country , Currency and PhoneCode apps
to django.

## Installation

To install this package run
`pip install django-country-utils`

## Usage

To use it add to settings.py

``` python

INSTALLED_APPS = [
    ...
    'currency',
    'country',
    'phonecode',
    ...
]

```

To use it add to settings.py

``` python
python manage.py loaddata country
```
