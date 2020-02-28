from rest_framework import serializers
from . import models


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='game-detail')

    class Meta:
        model = models.GameCategory
        fields = ('url', 'pk', 'name', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(queryset=models.GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = models.Game
        fields = ('url', 'category', 'name', 'release_date', 'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = models.PlayerScore
        fields = ('url', 'pk', 'score', 'score_date', 'game')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.ChoiceField(choices=models.Player.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = models.Player
        fields = ('url', 'name', 'gender', 'gender_description', 'scores')


class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=models.Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=models.Game.objects.all(), slug_field='name')

    class Meta:
        model = models.PlayerScore
        fields = ('url', 'pk', 'score', 'score_date', 'player', 'game')
