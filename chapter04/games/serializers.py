from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='game-detail')     # omits view_name

    class Meta:
        model = models.GameCategory
        fields = ('url', 'pk', 'name', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=models.GameCategory.objects.all(), slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Game
        depth = 4       # omitted
        fields = ('url', 'owner', 'game_category', 'name', 'release_date', 'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = models.PlayerScore
        fields = ('url', 'pk', 'score', 'score_date', 'game')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.ChoiceField(choices=models.Player.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)     # omits read_only, source = 'get_gender_display'
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = models.Player
        fields = ('url', 'name', 'gender', 'gender_description', 'scores')


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(queryset=models.Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=models.Game.objects.all(), slug_field='name')

    class Meta:
        model = models.PlayerScore
        fields = ('url', 'pk', 'score', 'score_date', 'player', 'game')


# Make Serializer for field games in UserSerializer
class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Game
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'games')
