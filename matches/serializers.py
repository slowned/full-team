from matches.models import Match
from rest_framework import serializers

from players.models import PlayerProfile


class MatchSerializer(serializers.ModelSerializer):
    """ Serialize/deserialize Matches """
    # players = serializers.SerializerMethodField()

    class Meta:
        """ Available filds to show/recive """

        model = Match
        fields = [
            'owner',
            'start',
            'end',
            'capacity',
            'price',
        ]

