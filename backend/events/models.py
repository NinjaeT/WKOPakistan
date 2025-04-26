from django.db import models
from accounts.models import FamilyProfile


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    family = models.ForeignKey(FamilyProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
