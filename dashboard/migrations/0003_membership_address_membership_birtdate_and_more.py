# Generated by Django 4.1.2 on 2022-10-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='birtdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='place_of_birth',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
