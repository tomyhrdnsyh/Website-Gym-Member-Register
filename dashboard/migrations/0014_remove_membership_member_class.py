# Generated by Django 4.1.2 on 2023-01-01 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_membershipdetail_alter_membership_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='member_class',
        ),
    ]
