# Generated by Django 3.2.4 on 2021-07-05 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_device_device_mac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washroom',
            name='bath_filled',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='pot_filled',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='urinal_filled',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='waterpoint',
            name='device',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='device.device'),
        ),
    ]
