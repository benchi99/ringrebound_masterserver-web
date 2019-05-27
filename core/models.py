from django.db import models


class GameServer(models.Model):
    name = models.CharField(max_length=40)
    number_players = models.BigIntegerField()
    ip_address = models.CharField(max_length=15)
    port = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
