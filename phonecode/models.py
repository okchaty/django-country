from django.db import models
from model_utils.models import TimeStampedModel
from .utils import InvalidMobileLength


class PhoneCodeQuerySet(models.QuerySet):
    def get_by_country_code(self, country_code):
        return self.filter(country__code=country_code).first()

    def validate_mobile(self, country_code, mobile):
        """
        Validates the lenght of the given mobile phone in E.104
        based on the country code.

        mobile: Normalize mobile phone in E.164
        """
        phone_code = self.get_by_country_code(country_code)
        phone_code.validate_mobile(mobile)


class PhoneCode(TimeStampedModel):
    country = models.ForeignKey(
        "country.Country",
        on_delete=models.CASCADE,
        related_name="phone_codes")
    code = models.CharField(
        max_length=20,
        help_text="Phone code in E.164 format"
    )
    max_length = models.PositiveSmallIntegerField(
        help_text="Mobile phone max lenght for numbers in E.164 format"
    )
    min_length = models.PositiveSmallIntegerField(
        help_text="Mobile phone min lenght for numbers in E.164 format"
    )
    objects = PhoneCodeQuerySet.as_manager()

    def validate_mobile(self, mobile):
        """
        Validates the lenght of the given mobile phone in E.104
        based on the country code.

        mobile: Normalize mobile phone in E.164
        """

        if self.min_length <= len(mobile) <= self.max_length:
            return mobile
        raise InvalidMobileLength("Invalid mobile lenght")

    def __str__(self):
        return self.code

    class Meta:
        db_table = "phone_code"
        ordering = ["-created"]
