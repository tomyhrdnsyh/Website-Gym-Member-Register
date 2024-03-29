# Generated by Django 4.1.2 on 2022-10-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_place_of_birth_membership_birthplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('birth', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
