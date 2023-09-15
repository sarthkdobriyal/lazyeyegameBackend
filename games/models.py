from django.db import models

# Create your models here.
class PacmanData(models.Model):
    id = models.AutoField(primary_key=True)
    highscore = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
    playtime = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)


class RollexData(models.Model):
    id = models.AutoField(primary_key=True)
    highscore = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
    playtime = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)


class TetrisData(models.Model):
    id = models.AutoField(primary_key=True)
    highscore = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
    playtime = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    patient = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True, blank=False)
    