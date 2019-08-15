from rest_framework import serializers

from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    created_matches = serializers.StringRelatedField(many=True)

    class Meta:
        model = Player
        fields = [
            # TODO: extra_information: si el usuario acepta
            # telefono, giladas personales
            'username',
            'real_full_name',
            'locality',
            'created_matches',
        ]

