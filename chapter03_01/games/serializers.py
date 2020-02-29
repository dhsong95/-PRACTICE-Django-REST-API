from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.serializers import SlugRelatedField, HyperlinkedRelatedField, ChoiceField, CharField, ReadOnlyField
from .models import GameCategory, Game, Player, PlayerScore


class GameCategorySerializer(HyperlinkedModelSerializer):
    games = HyperlinkedRelatedField(many=True, read_only=True, view_name='game-detail')

    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games')


class GameSerializer(HyperlinkedModelSerializer):
    game_category = SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        depth = 4
        fields = ('url', 'owner', 'game_category', 'name', 'release_date', 'played')


class ScoreSerializer(HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = ('url', 'pk', 'score', 'score_date', 'game')


class PlayerSerializer(HyperlinkedModelSerializer):
    gender = ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = CharField(source='get_gender_display', read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url', 'name', 'gender', 'gender_description', 'scores')


class PlayerScoreSerializer(ModelSerializer):
    player = SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game = SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = ('url', 'pk', 'score', 'score', 'score_date', 'player', 'game')


class UserGameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name')


class UserSerializer(HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'games')
