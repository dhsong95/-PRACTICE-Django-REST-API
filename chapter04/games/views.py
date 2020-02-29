from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import ScopedRateThrottle
from . import models
from . import serializers
from . import permissions
from . import filters


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
    throttle_scope = 'game-categories'
    throttle_classes = [ScopedRateThrottle, ]
    filter_fields = ('name', )
    search_fields = ('^name', )
    ordering_fields = ('name', )


class GameCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.GameCategory.objects.all()
    serializer_class = serializers.GameCategorySerializer
    name = 'gamecategory-detail'
    throttle_scope = 'game-categories'
    throttle_classes = [ScopedRateThrottle, ]


class GameList(ListCreateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    name = 'game-list'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly,
    ]
    filter_fields = ('name', 'game_category', 'release_date', 'played', 'owner', )
    search_filed = ('^name', )
    ordering_fields = ('name', 'release_date', )

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
    filter_fields = ('name', 'gender', )
    search_fields = ('^name', )
    ordering_fields = ('name', )


class PlayerDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(ListCreateAPIView):
    queryset = models.PlayerScore.objects.all()
    serializer_class = serializers.PlayerScoreSerializer
    name = 'playerscore-list'
    filter_class = filters.PlayerScoreFilter
    ordering_fields = ('score', 'score_date', )


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
