# Generated by Django 3.2.4 on 2021-07-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_device_type_availaable_credit_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_type_availaable',
            name='credit_rate',
        ),
    ]
