# Generated by Django 5.2.3 on 2025-07-03 11:46

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userinformation', '0010_user_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
    ]
