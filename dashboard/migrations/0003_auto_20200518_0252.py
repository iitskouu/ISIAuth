# Generated by Django 3.0.6 on 2020-05-18 01:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200518_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]