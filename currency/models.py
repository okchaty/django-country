from django.db import models
from model_utils.models import TimeStampedModel


class Currency(TimeStampedModel):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=45, blank=True, null=True)
    currency_symbol = models.CharField(max_length=3, blank=True)
    currency_format = models.CharField(max_length=40, blank=True, null=True)
    number_format = models.CharField(max_length=40, blank=True, null=True)
    
    class Meta:
        db_table = "currency"
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.name
