# Generated by Django 4.0.6 on 2022-12-30 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='zip_code',
            new_name='zipcode',
        ),
    ]
