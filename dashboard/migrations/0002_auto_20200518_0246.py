# Generated by Django 3.0.6 on 2020-05-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
