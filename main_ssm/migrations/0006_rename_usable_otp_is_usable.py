# Generated by Django 3.2.1 on 2021-05-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_ssm', '0005_otp_usable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='usable',
            new_name='is_usable',
        ),
    ]