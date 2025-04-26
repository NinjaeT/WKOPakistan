from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
