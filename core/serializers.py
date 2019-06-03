from rest_framework import serializers

from .models import GameServer


class GameServerSeralizer(serializers.Serializer):
    name = serializers.CharField()
    number_players = serializers.IntegerField()
    ip_address = serializers.CharField(allow_null=True, allow_blank=True)
    port = serializers.IntegerField()

    def create(self, validated_data):
        return GameServer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number_players = validated_data.get('number_players', instance.number_players)
        instance.ip_address = validated_data.get('ip_address', instance.ip_address)
        instance.port = validated_data.get('port', instance.port)

        instance.save()
        return instance


