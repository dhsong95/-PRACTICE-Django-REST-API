from django_filters.filters import NumberFilter, DateTimeFilter, AllValuesFilter
from rest_framework import filters
from .models import PlayerScore


class PlayerScoreFilter(filters.SearchFilter):
    min_score = NumberFilter(field_name='score', lookup_expr='gte')
    max_score = NumberFilter(field_name='score', lookup_expr='lte')
    from_score_date = DateTimeFilter(field_name='score_date', lookup_expr='gte')
    to_scoreD_date = DateTimeFilter(field_name='scored_date', lookup_expr='lte')
    player_name = AllValuesFilter(field_name='player__name')
    game_name = AllValuesFilter(field_name='game__name')

    class Meta:
        model = PlayerScore
        fields = ('score', 'from_score_date', 'to_score_date', 'min_score', 'max_score', 'player_name', 'game_name')
