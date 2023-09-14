from rest_framework import serializers
from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'id', 'is_doctor', 'name', 'is_superuser', 'created_date')