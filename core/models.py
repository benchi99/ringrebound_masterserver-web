from django.db import models
from django.db.models import manager


class GameServerManager(manager.Manager):
    def get_queryset(self):
        return GameServerQuerySet(self.model, using=self._db)


class GameServerQuerySet(models.QuerySet):
    pass


class GameServer(models.Model):
    name = models.CharField(max_length=40)
    number_players = models.BigIntegerField()
    ip_address = models.CharField(max_length=15)
    port = models.PositiveSmallIntegerField()

    objects = GameServerManager.from_queryset(GameServerQuerySet)()

    def __str__(self):
        return self.name
