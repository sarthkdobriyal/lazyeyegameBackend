from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer
from accounts.models import DoctorPatientRelationship, Account

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def signup(request):
    if request.data['role'] == 1 or request.data['role'] == 2  and request.user.role != 1:
        return Response("Error", status=status.HTTP_401_UNAUTHORIZED)
    print(request.data)
    serializer = UserSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print("valid")
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        if request.user.role == 2:
            print(request.user.id, user.id)
            doctor = Account.objects.get(id=request.user.id)
            patient = Account.objects.get(id=user.id)
            DoctorPatientRelationship.objects.create(doctor=doctor, patient=patient)
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.username))