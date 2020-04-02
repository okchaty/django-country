from babel.numbers import format_decimal
from django.db import models
from model_utils.models import TimeStampedModel


class CurrencyManager(models.Manager):

    def get_by_natural_key(self, abbreviation):
        return self.get(abbreviation=abbreviation)

    def format_money(self, money, currency_abbreviation="PEN"):
        currrency = self.get_by_natural_key(currency_abbreviation)
        country = currency.countries.first()
        amount_formated = format_decimal(
            money,
            format=currency.number_format,
            locale="{}_{}".format(country.language, country.code),
        )
        return currency.currency_format.format(amount_formated)


class Currency(TimeStampedModel):
    abbreviation = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=5)
    currency_format = models.CharField(max_length=45)
    number_format = models.CharField(max_length=45)

    objects = CurrencyManager()
    
    class Meta:
        db_table = "currency"
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.name
