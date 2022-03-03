from django.db import models
from email.errors import MalformedHeaderDefect

# Create your models here.


class Students(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    standard = models.CharField(max_length=64)
    stream = models.CharField(max_length=64)
    telephone = models.CharField(max_length=64)
    email_address = models.CharField(max_length=64)
    father_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first} {self.last}"


class Reports(models.Model):
    candidate = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="obtainer")
    year = models.IntegerField()

