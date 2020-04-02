from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


def populate_data(sender, **kwargs):
    call_command("loaddata", "country", verbosity=1)


class CountryConfig(AppConfig):
    name = 'country'

    def ready(self):
        post_migrate.connect(populate_data, sender=self)
