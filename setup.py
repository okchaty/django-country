from setuptools import setup


setup(
    packages=[
        "country.management",
        "country.management.commands",
        "country.fixtures",
        "country.migrations",
        "country",
        "currency",
        "currency.migrations",
        "phonecode",
        "phonecode.migrations",
    ],
)
