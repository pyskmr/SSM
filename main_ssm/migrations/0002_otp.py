# Generated by Django 3.2.1 on 2021-05-25 11:49

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_ssm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('otp_sent', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_blocked', models.DateTimeField(null=True)),
                ('attempts', models.PositiveIntegerField(default=0)),
                ('otp_type', models.CharField(choices=[('two_factor', 'two_factor'), ('phone_verification', 'phone_verification'), ('forgot_password', 'forgot_password'), ('payment', 'payment')], max_length=255)),
            ],
        ),
    ]
