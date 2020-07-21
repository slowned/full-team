from rest_framework import viewsets

from players.models import PlayerProfile
from players.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerSerializer

    class Meta:
        model = PlayerProfile
