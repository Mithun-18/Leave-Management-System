# Generated by Django 5.0.6 on 2024-07-17 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lm_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_id',
        ),
    ]
