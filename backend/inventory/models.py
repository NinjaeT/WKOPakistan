from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="inventory/images/", blank=True, null=True
    )

    def __str__(self):
        return self.name
