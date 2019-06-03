from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ipware import get_client_ip

from .models import GameServer
from .serializers import GameServerSeralizer


class GameServerList(APIView):
    """
    Listar todos los servidores, o crear uno nuevo.
    """
    def get(self, request, format=None):
        gameservers = GameServer.objects.all()
        serializer = GameServerSeralizer(gameservers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        ip, is_routeable = get_client_ip(request)
        if ip:
            server_data = request.data.dict()
            server_data['ip_address'] = str(ip)

            serializer = GameServerSeralizer(data=server_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data={'error': True, 'reason': 'Could not obtain IP address.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class GameServerDetail(APIView):
    """
    Obtén o elimina una instancia de servidor.
    """

    def get_object(self, id):
        try:
            return GameServer.objects.get(id=id)
        except Exception:
            raise Http404

    def get(self, request, id, format=None):
        gameserver = self.get_object(id)
        serializer = GameServerSeralizer(gameserver)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        gameserver = self.get_object(id)
        gameserver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class GameServerViewSet(viewsets.ModelViewSet):
#     queryset = GameServer.objects.all()
#     serializer_class = GameServerSeralizer
