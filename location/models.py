from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.region}, {self.city}, {self.country}, {self.zipcode}"