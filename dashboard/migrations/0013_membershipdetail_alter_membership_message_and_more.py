# Generated by Django 4.1.2 on 2023-01-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_membership_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_class', models.CharField(max_length=254)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='membership',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='member_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.membershipdetail'),
        ),
    ]