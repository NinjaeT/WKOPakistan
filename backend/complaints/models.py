from django.db import models
from accounts.models import FamilyProfile


class Complaint(models.Model):
    family = models.ForeignKey(FamilyProfile, on_delete=models.CASCADE)
    text = models.TextField()
    status = [("open", "Open"), ("done", "Done")]
    created = models.DateTimeField(auto_now_add=True)
