from rest_framework import serializers
from .models import *


class PacmanSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PacmanData
        fields = '__all__'

class RollexSerializer(serializers.ModelSerializer):
    class Meta:
        model =  RollexData
        fields = '__all__'

class TetrisSerializer(serializers.ModelSerializer):
    class Meta:
        model =  TetrisData
        fields = '__all__'
        
class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  GameData
        fields = '__all__'