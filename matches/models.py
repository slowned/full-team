from django.db import models
from players.models import PlayerProfile


class Match(models.Model):
    #TODO: evaluar atributo end
    owner = models.ForeignKey(PlayerProfile, related_name='created_matches', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    capacity = models.IntegerField()  # choice field 5, 7, 9, 11
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # amount ?
    players = models.ManyToManyField(PlayerProfile)

    def __str__(self):
        return 'Dia: {}, Hora: {}'.format(self.start, self.end)
