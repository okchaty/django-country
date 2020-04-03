from os.path import exists
from setuptools import setup


setup(
    name="django-country-utils",
    version="0.2.8",
    author="Chaty",
    author_email="develop@okchaty.com",
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
    include_package_data=True,
    scripts=[
        "country.fixtures.country.yaml",
    ],
    url="https://github.com/okchaty/django-country",
    license="MIT License",
    description="Support for generic apps of country, currencies and phonecodes.",
    long_description=open("README.md").read() if exists("README.md") else "",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=["Django>=1.11", "Babel", "django-model-utils"],
    zip_safe=False,
)
