from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """Get all patients created by the authenticated user"""
        patients = Patient.objects.filter(user=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new patient"""
        serializer = PatientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get details of a specific patient"""
        patient = get_object_or_404(Patient, id=pk, user=request.user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Update patient details"""
        patient = get_object_or_404(Patient, id=pk, user=request.user)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """Delete a patient record"""
        patient = get_object_or_404(Patient, id=pk, user=request.user)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)