# Generated by Django 4.1.2 on 2023-01-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_payment_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='active_status',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
