from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Flavor(models.Model):
    flavor = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    rating = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(1), MinValueValidator(10)]
     )

    def __str__(self):
        return self.name

# class Description(models.Model):
#     description = models.TextField()

#     flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)

#     user = models.ForeignKey(User, on_delete=models.CASCADE) 