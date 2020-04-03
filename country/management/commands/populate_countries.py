from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from os import path


class Command(BaseCommand):
    help = "Populates data"

    def handle(self, *args, **options):
        fixture_path = path.join(path.dirname(
            path.dirname(
                path.dirname(
                    path.abspath(__file__)
                )
            )
        ), "fixtures/")
        settings.FIXTURE_DIRS = (fixture_path,)
        call_command("loaddata", "country", verbosity=1)
