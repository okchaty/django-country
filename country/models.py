from django.contrib.postgres.fields import JSONField
from django.db import models
from model_utils.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45, unique=True)
    language = models.CharField(max_length=45)
    extra = JSONField(blank=True, null=True)
    currency = models.ForeignKey(
        "currency.Currency",
        on_delete=models.CASCADE,
        related_name="countries",
    )

    class Meta:
        db_table = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name
