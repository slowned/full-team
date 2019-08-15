from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from matches.views import MatchViewSet
from players.views import PlayerViewSet

router = routers.DefaultRouter()
router.register(
    r'players',
    PlayerViewSet,
)
router.register(
    r'matches',
    MatchViewSet,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include((router.urls, 'api'))),
]

