from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)


BELT_RANK_CHOICES = [
    ("white", "White"),
    ("red", "Red"),
    ("blue", "Blue"),
    ("yellow", "Yellow"),
    ("green", "Green"),
    ("brown", "Brown"),
    ("black", "Black"),
]

DAN_CHOICES = [
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    ("9th", "9th"),
    ]


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    roll_no = models.CharField(max_length=20)
    belt_rank = models.CharField(
        max_length=6,
        choices=BELT_RANK_CHOICES,
        default="white",
    )
    dan = models.CharField(
        max_length=3,
        choices=DAN_CHOICES,
        null=True,
        blank=True,
        default=None,
    )


class FamilyProfile(models.Model):
    family_name = models.CharField(max_length=100)  # e.g. “Khilji Brothers”
    family_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="families_admin"
    )
    family_members = models.ManyToManyField(
        UserProfile, related_name="families_members"
    )
