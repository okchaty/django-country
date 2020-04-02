# Generated by Django 3.0.4 on 2020-04-02 18:16

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('abbreviation', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('currency_symbol', models.CharField(max_length=5)),
                ('currency_format', models.CharField(max_length=45)),
                ('number_format', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'currencies',
                'db_table': 'currency',
            },
        ),
    ]
