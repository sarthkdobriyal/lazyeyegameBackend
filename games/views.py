from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.models import DoctorPatientRelationship, Account
from .models import *
from .serializers import *
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
def editGameSpecs(request,game, patientid):
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

            
            return Response("Game Specs updated successfully for {}".format(patient.username))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)




@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editGameData(request, game, patientid):
    if request.user.role == 3:
        try:
            # Get the patient from the database
            patient = Account.objects.get(id=patientid)
            print(patient)
            model = game_models.get(game)
            print(model)
            if model is None:
                return Response("Invalid game: {}".format(game), status=status.HTTP_400_BAD_REQUEST)

            gameData = GameData.objects.create(patient=patient, game=game, highscore=request.data['highscore'], playtime=request.data['playtime'])
            return Response("Game Data updated successfully for {}".format(patient.username))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getGameData(request, game, patientid):
    try:
        # Get the patient from the database
        patient = Account.objects.get(id=patientid)
        print(patient)
        model = game_models.get(game)
        print(model)
        if model is None:
            return Response("Invalid game: {}".format(game), status=status.HTTP_400_BAD_REQUEST)

        gameData = GameData.objects.filter(patient=patient, game=game)
        game_data = GameDataSerializer(gameData, many=True).data
        return Response(game_data, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


