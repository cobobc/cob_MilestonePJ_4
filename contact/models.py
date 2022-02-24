from django.db import models

# Create your models here.


class Contact(models.Model):
    """
    A Contact model for staff to view users queries
    """
    subject = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.CharField(max_length=60, null=False, blank=False)
    comments = models.CharField(max_length=2000, null=False, blank=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
