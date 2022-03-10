# Generated by Django 4.0.2 on 2022-03-09 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=50)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('father_name', models.CharField(max_length=64, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=64, null=True)),
                ('standard', models.CharField(max_length=10, null=True)),
                ('roll_number', models.IntegerField(default=0, null=True)),
                ('telephone', models.IntegerField(default=0, null=True)),
                ('residence', models.TextField(default=0)),
                ('url', models.URLField(blank=True, null=True)),
                ('profile_pic', models.FileField(default=0, upload_to='')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8')], max_length=64, null=True)),
                ('physics', models.FloatField(default=0, null=True)),
                ('maths', models.FloatField(default=0, null=True)),
                ('biology', models.FloatField(default=0, null=True)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('student_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.student')),
            ],
        ),
    ]
