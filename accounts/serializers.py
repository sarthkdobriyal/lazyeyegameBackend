from rest_framework import serializers
from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'username', 'password', 'email', 'role', "firstname", "lastname"
        ]

    def validate(self, data): 
        print(data)
        return super().validate(data)
    
    def create(self, validated_data):
        role = validated_data['role']
        print( 'Rolee->', role)
        if role == 3:
            user = Account.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                firstname=validated_data['firstname'],
                lastname=validated_data['lastname'],
                password=validated_data['password'],
                role=validated_data['role'],
        )
            user.set_password(validated_data['password'])
            user.save()
            return user
        elif role == 2:
            user = Account.objects.create_staffuser(
                email=validated_data['email'],
                username=validated_data['username'],
                firstname=validated_data['firstname'],
                lastname=validated_data['lastname'],
                password=validated_data['password'],
                role=validated_data['role'],
        )
            user.set_password(validated_data['password'])
            user.save()
            return user