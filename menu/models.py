from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class BestItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, default=False)
    image = CloudinaryField('image', blank=False, default=False)

    def __str__(self):
        return str(self.name) + " " + str(self.price)