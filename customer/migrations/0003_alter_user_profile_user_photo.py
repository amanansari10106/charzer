# Generated by Django 3.2.4 on 2021-06-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_user_profile_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_photo',
            field=models.ImageField(default='default_profile_img.jpg', upload_to='images/'),
        ),
    ]
