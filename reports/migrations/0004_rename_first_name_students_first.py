# Generated by Django 4.0.2 on 2022-03-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_reports_physics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='first_name',
            new_name='first',
        ),
    ]
