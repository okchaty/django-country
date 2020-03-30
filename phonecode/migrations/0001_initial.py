# Generated by Django 3.0.3 on 2020-03-30 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(help_text='Phone code in E.164 format', max_length=20)),
                ('max_length', models.PositiveSmallIntegerField(help_text='Mobile phone max lenght for numbers in E.164 format')),
                ('min_length', models.PositiveSmallIntegerField(help_text='Mobile phone min lenght for numbers in E.164 format')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_codes', to='country.Country')),
            ],
            options={
                'db_table': 'phone_code',
                'ordering': ['-created'],
            },
        ),
    ]
