from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GameCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Game(models.Model):
    owner = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    game_category = models.ForeignKey(GameCategory, related_name='games', on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Player(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True, blank=True, default='')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='M')

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        ordering = ('-score', )
