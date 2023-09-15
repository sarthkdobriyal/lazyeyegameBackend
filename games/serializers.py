from rest_framework import serializers
from .models import PacmanData, RollexData, TetrisData


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