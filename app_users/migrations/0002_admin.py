# Generated by Django 5.1.1 on 2024-10-01 13:47

import app_users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app_users.usermodel',),
            managers=[
                ('objects', app_users.managers.AdminManager()),
            ],
        ),
    ]