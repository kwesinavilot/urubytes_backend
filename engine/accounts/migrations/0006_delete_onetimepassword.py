# Generated by Django 5.0.3 on 2024-03-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_onetimepassword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OneTimePassword',
        ),
    ]
