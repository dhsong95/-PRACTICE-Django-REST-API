from django.urls import path
from .views import game_list, game_detail

app_name = 'games'

urlpatterns = [
    path('', game_list, name='list'),
    path('<int:pk>/', game_detail, name='detail'),
]
