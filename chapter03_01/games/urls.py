from django.urls import path
from . import views


urlpatterns = [
    path('', views.APIRoot.as_view(), name=views.APIRoot.name),
    path('games/', views.GameList.as_view(), name=views.GameList.name),
    path('game/<int:pk>/', views.GameDetail.as_view(), name=views.GameDetail.name),
    path('game-categories/', views.GameCategoryList.as_view(), name=views.GameCategoryList.name),
    path('game-category/<int:pk>/', views.GameCategoryDetail.as_view(), name=views.GameCategoryDetail.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('player/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    path('player-scores/', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    path('player-score/<int:pk>', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
]