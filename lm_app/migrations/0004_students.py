# Generated by Django 5.0.6 on 2024-07-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lm_app', '0003_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('leave_type', models.CharField(max_length=8)),
                ('reason', models.TextField(max_length=200)),
                ('status', models.CharField(default='Pending', max_length=12)),
            ],
        ),
    ]