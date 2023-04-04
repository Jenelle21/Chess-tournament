from django.db import models


class Game(models.Model):
    white_player = models.CharField(max_length=255)
    black_player = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=5)


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    move_number = models.IntegerField()
    color = models.CharField(max_length=5)
    move_san = models.CharField(max_length=10)
    analysis = models.IntegerField()
