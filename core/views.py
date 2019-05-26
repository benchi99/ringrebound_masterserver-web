# from django.http import HttpResponse
from rest_framework import viewsets

from .models import GameServer
from .serializers import GameServerSeralizer


class GameServerViewSet(viewsets.ModelViewSet):
    queryset = GameServer.objects.all()
    serializer_class = GameServerSeralizer
