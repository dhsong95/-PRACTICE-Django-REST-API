from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import models
from . import serializers
from . import permissions


# Create your views here.
class APIRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request,  *args, **kwargs):
        return Response({
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'players': reverse(PlayerList.name, request=request),
            'player-scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request),
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
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    name = 'game-detail'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly,
    ]


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


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-list'


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-detail'
