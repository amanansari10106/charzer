# Generated by Django 3.2.4 on 2021-07-04 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('organization_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance_money', models.FloatField()),
                ('bank_acc_no', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_acc_name', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='organization_agent_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_agent_phone', models.IntegerField()),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
    ]
