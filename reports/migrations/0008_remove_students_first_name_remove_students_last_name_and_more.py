# Generated by Django 4.0.2 on 2022-03-07 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0007_rename_first_students_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='last_name',
        ),
        migrations.AddField(
            model_name='students',
            name='first',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='last',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
