# Generated by Django 4.1 on 2022-08-19 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='member',
            field=models.CharField(max_length=200),
        ),
    ]
