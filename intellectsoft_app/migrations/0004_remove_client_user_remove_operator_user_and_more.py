# Generated by Django 5.0.2 on 2024-02-10 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intellectsoft_app', '0003_client_user_request_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='user',
        ),
        migrations.RemoveField(
            model_name='request',
            name='client',
        ),
    ]
