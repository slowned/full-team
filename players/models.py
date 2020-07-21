from django.db import models
from players import constants as cts


class PlayerProfile(models.Model):
    # Personal data
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    cell_phone = models.CharField(max_length=40, null=False)
    gender = models.CharField(
        max_length=1, choices=cts.GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        """ Generate a useful representation. """
        return f"{self.name} {self.surname} ({self.pk})"
