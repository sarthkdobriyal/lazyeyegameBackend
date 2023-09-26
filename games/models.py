from django.db import models

# Create your models here.
class PacmanData(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)


class RollexData(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)


class TetrisData(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)
    

class GameData(models.Model):
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)
    game = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    highscore = models.PositiveIntegerField(default=0)
    playtime = models.PositiveIntegerField(default=0)