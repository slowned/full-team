import unidecode

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from players import constants as cts


# class User(AbstractUser):
#     email = models.EmailField(
#         _('email address'), unique=True, blank=False, db_index=True)
#   date_joined    


# TODO: generar red social
class Player(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # friend_list = models.ManyToManyField(User)  # la relacion deberia ser con player
    username = models.CharField(max_length=20)
    # Personal data
    birth_date = models.DateField()
    cell_phone = models.CharField(max_length=40)
    real_full_name = models.CharField(max_length=60)
    gender = models.CharField(
        max_length=1, choices=cts.GENDER_CHOICES, blank=True, null=True)
    locality = models.TextField(blank=True, null=True, default='')
    postal_code = models.CharField(
        max_length=50, blank=True, null=True, default='')
    province = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        """ Generate a useful representation. """
        name = ''
        if self.real_full_name:
            name = unidecode.unidecode(self.real_full_name)
        return "{}, {}".format(name, self.pk)
