# Generated by Django 5.2.3 on 2025-07-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinformation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_number',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
