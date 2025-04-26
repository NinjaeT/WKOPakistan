from django.db import models
from accounts.models import FamilyProfile


class Reminder(models.Model):
    family = models.ForeignKey(FamilyProfile, on_delete=models.CASCADE)
    text = models.CharField()
    remind_at = models.DateTimeField()
    sent = models.BooleanField(default=False)
