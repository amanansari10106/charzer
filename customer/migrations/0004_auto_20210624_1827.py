# Generated by Django 3.2.4 on 2021-06-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_user_profile_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_photo',
            field=models.ImageField(default='images/profileimage/default_profile_img.jpg', null=True, upload_to='images/profileimage/'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_type',
            field=models.CharField(default='customer', max_length=20),
        ),
    ]
