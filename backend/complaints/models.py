from django.db import models
from accounts.models import FamilyProfile


class Complaint(models.Model):
    title = models.CharField(max_length=255)
    family = models.ForeignKey(FamilyProfile, on_delete=models.CASCADE)
    text = models.TextField()
    status = [("open", "Open"), ("done", "Done")]
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
