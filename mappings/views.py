from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """Get all patient-doctor mappings"""
        mappings = PatientDoctorMapping.objects.filter(user=request.user)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Assign a doctor to a patient"""
        serializer = PatientDoctorMappingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get all doctors assigned to a specific patient"""
        # Here pk is the patient_id
        mappings = PatientDoctorMapping.objects.filter(user=request.user, patient_id=pk)
        if not mappings.exists():
            return Response({"detail": "No mappings found for this patient"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        """Remove a doctor from a patient"""
        mapping = get_object_or_404(PatientDoctorMapping, id=pk, user=request.user)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)