# Generated by Django 4.1 on 2022-08-17 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='time_zone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]