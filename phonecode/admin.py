from django.contrib import admin
from .models import PhoneCode


@admin.register(PhoneCode)
class PhoneCodeAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "code",
        "max_length",
        "min_length",
        "created",
        "modified",
    )
    raw_id_fields = ("country",)
