# Generated by Django 4.1 on 2022-08-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_message_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='token',
        ),
        migrations.RemoveField(
            model_name='room',
            name='uid',
        ),
    ]
