
from email.policy import default
from django.db import models
from email.errors import MalformedHeaderDefect
from django.contrib.auth.models import User
# from django.conf import settings


from reports.views import scores


class Students(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    first = models.CharField(null=True, max_length=64)
    last = models.CharField(null=True, max_length=64)
    standard = models.CharField(max_length=64)
    stream = models.CharField(max_length=64)
    telephone = models.CharField(max_length=64)
    email_address = models.CharField(max_length=64)
    father_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first} {self.last}"


class Reports(models.Model):
    candidate = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="obtainer")
    semester = models.IntegerField()
    Physics = models.FloatField()
    # Maths = models.FloatField(default=0)
  
