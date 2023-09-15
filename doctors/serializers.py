from rest_framework import serializers
from accounts.models import Account


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'firstname', 'lastname', 'created_date', 'id', 'category', 'contactno', 'dob', 'gender', 'location', 'mrdnumber' ]