from django.db import models


class GameServer(models.Model):
    id = models.BigAutoField()
    name = models.CharField()
    number_players = models.BigIntegerField()
    ip_address = models.CharField()
    port = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
