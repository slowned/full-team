from django.db import models
from players.models import Player


class Match(models.Model):
    #TODO: evaluar atributo end
    owner = models.ForeignKey(Player, related_name='created_matches', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateField()
    capacity = models.IntegerField()  # slots ?
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # amount ?
    # player = models.ManyToManyField('player.Player')

    def __str__(self):
        return 'Dia: {}, Hora: {}'.format(self.start, self.end)
