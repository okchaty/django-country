from django.contrib import admin
from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "language",
        "extra",
        "currency"
    )
    raw_id_fields = ("currency",)
