from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    """
    Input fields for beat genre
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Beat(models.Model):
    """
    Input fields adding new beat
    """
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    file = models.FileField(upload_to='media/', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Input fields for adding reviewing a beat
    """
    beat = models.ForeignKey(
        'Beat', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
