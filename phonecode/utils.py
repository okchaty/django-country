# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError


class DoesNotAvailablePhone(ValidationError):
    pass


class InvalidMobileCountry(ValidationError):
    pass


class InvalidMobileLength(ValidationError):
    pass
