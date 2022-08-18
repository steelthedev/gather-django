# Generated by Django 4.1 on 2022-08-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('room', models.CharField(max_length=300)),
                ('uid', models.CharField(max_length=200)),
            ],
        ),
    ]