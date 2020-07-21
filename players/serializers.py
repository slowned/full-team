from rest_framework import serializers

from players.models import PlayerProfile


class PlayerSerializer(serializers.ModelSerializer):
    # created_matches = serializers.StringRelatedField(many=True)

    class Meta:
        model = PlayerProfile
        fields = [
            'name',
            'surname',
            'username',
            'cell_phone',
            'gender',
        ]
