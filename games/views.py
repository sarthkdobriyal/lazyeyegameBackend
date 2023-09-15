from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.models import DoctorPatientRelationship, Account
from .models import PacmanData, RollexData, TetrisData
from .serializers import PacmanSerializer, RollexSerializer, TetrisSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

game_models = {
    'pacman': PacmanData,
    'rollex': RollexData,
    'tetris': TetrisData,
}




@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editGame(request,game, patientid):
    if request.user.role == 2:
        try:
            # Get the patient from the database
            patient = Account.objects.get(id=patientid)
            print(patient)
            model = game_models.get(game)
            print(model)
            if model is None:
                return Response("Invalid game: {}".format(game), status=status.HTTP_400_BAD_REQUEST)

            try:
                gameData = model.objects.get(patient=patient)
            except ObjectDoesNotExist:
                gameData = model.objects.create(patient=patient)

            for field in request.data:
                if hasattr(gameData, field):
                    print(field)
                    setattr(gameData, field, request.data[field])
                else:
                    return Response("Invalid field: {}".format(field), status=status.HTTP_400_BAD_REQUEST)
            gameData.save()

            
            return Response("Game data updated successfully for {}".format(patient.username))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)

