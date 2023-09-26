from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.models import DoctorPatientRelationship, Account
from .serializers import PatientSerializer
from games.models import PacmanData, RollexData, TetrisData
from games.serializers import PacmanSerializer, RollexSerializer, TetrisSerializer

# Create your views here.

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPatients(request):
    print(request.user.role)
    if(request.user.role == 2):
        #get all the entries from doctorpatientrelationship where doctor is the current user in the list
        patient_ids = DoctorPatientRelationship.objects.filter(doctor=request.user).values_list('patient_id', flat=True)
        #get all the patients from the entries
        if(request.GET.get('category')):
            patients = Account.objects.filter(id__in=patient_ids, category=request.GET.get('category'))
        else:
            patients = Account.objects.filter(id__in=patient_ids)
        print(patients)
        #return the patients
        serializer = PatientSerializer(patients, many=True)
        # print(serializer.data)
        #loop over the patients and get Game data for each patient
        patient_data_list = serializer.data
        resdata = {}
        for patient in patient_data_list:
            print(patient['id'])
            gameSpecs = {}
            try:
                pacmanData = PacmanData.objects.get(patient=patient['id'])
                gameSpecs['pacman'] = PacmanSerializer(pacmanData).data
            except PacmanData.DoesNotExist:
                gameSpecs['pacman'] = {}
            try:
                rollexData = RollexData.objects.get(patient=patient['id'])
                gameSpecs['rollex'] = RollexSerializer(rollexData).data
            except RollexData.DoesNotExist:
                gameSpecs['rollex'] = {}  # Add an empty object if data is not available
            try:
                tetrisData = TetrisData.objects.get(patient=patient['id'])
                gameSpecs['tetris'] = TetrisSerializer(tetrisData).data
            except TetrisData.DoesNotExist:
                gameSpecs['tetris'] = {}
            
            patient['gameSpecs'] = gameSpecs
        resdata['patients'] = patient_data_list
        return Response(resdata, status=status.HTTP_200_OK)
    return Response("passed for {}".format(request.user.username))



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPatient(request, id):
    if(request.user.role == 2):
        
        print("hello")
        #Check if the doctor patient relnship exists for this user
        if not DoctorPatientRelationship.objects.filter(patient=id, doctor=request.user.id).exists():
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)

        #get all the patients from the entries
        patient = Account.objects.get(id=id)
        print(patient)


        #return the patients
        serializer = PatientSerializer(patient)
        patient_data = serializer.data
        gameSpecs = {}
        try:
            pacmanData = PacmanData.objects.get(patient=id)
            gameSpecs['pacman'] = PacmanSerializer(pacmanData).data
        except PacmanData.DoesNotExist:
            gameSpecs['pacman'] = {}  # Add an empty object if data is not available

        try:
            rollexData = RollexData.objects.get(patient=id)
            gameSpecs['rollex'] = RollexSerializer(rollexData).data
        except RollexData.DoesNotExist:
            gameSpecs['rollex'] = {}  # Add an empty object if data is not available

        try:
            tetrisData = TetrisData.objects.get(patient=id)
            gameSpecs['tetris'] = TetrisSerializer(tetrisData).data
        except TetrisData.DoesNotExist:
            gameSpecs['tetris'] = {}
        patient_data['gameSpecs'] = gameSpecs
        return Response(patient_data, status=status.HTTP_200_OK)
    return Response({"error": "You are not authorized to view this patient"}, status=status.HTTP_401_UNAUTHORIZED)






@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editPatient(request, id):
    if request.user.role == 2:
        try:
            # Get the patient from the database
            patient = Account.objects.get(id=id)

            # Update patient fields with data from the request
            for field in request.data:
                if hasattr(patient, field):
                    setattr(patient, field, request.data[field])
                else:
                    return Response("Invalid field: {}".format(field), status=status.HTTP_400_BAD_REQUEST)
            
            # Save the updated patient data
            patient.save()
            
            return Response("Patient data updated successfully for {}".format(patient.username))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletePatient(request, id):
    if request.user.role == 2:
        try:
            # Get the patient from the database
            patient = Account.objects.get(id=id)

            # Update patient fields with data from the request
            # Save the updated patient data
            
            return Response("Patient Deleted {}".format(patient.username))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def togglePatientActive(request, id):
    if request.user.role == 2:
        try:
            # Get the patient from the database
            patient = Account.objects.get(id=id)

            # Update patient fields is_active to opposite
            patient.is_active = not patient.is_active
            # Save the updated patient data
            patient.save()
            
            return Response("Patient set to  {}".format(patient.is_active))
        except Account.DoesNotExist:
            return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("Error", status=status.HTTP_401_UNAUTHORIZED)


