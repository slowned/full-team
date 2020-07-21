from rest_framework import routers

from matches.views import MatchViewSet
from players.views import PlayerViewSet

router = routers.DefaultRouter()

router.register(r'player', PlayerViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
