# Generated by Django 4.1.2 on 2022-10-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_membership_disability_disease_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='birtdate',
            new_name='birthdate',
        ),
    ]
