from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import serializers
from . import models


# Create your views here.
class APIRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'player-scores': reverse(PlayerScoreList.name, request=request)
        })


class GameCategoryList(ListCreateAPIView):
    queryset = models.GameCategory.objects.all()
    serializer_class = serializers.GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.GameCategory.objects.all()
    serializer_class = serializers.GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(ListCreateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    name = 'game-list'


class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    name = 'game-detail'


class PlayerList(ListCreateAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    name = 'player-list'


class PlayerDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(ListCreateAPIView):
    queryset = models.PlayerScore.objects.all()
    serializer_class = serializers.PlayerScoreSerializer
    name = 'playerscore-list'


class PlayerScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.PlayerScore.objects.all()
    serializer_class = serializers.PlayerScoreSerializer
    name = 'playerscore-detail'
