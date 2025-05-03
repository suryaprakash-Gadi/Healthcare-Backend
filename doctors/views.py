from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """Get all doctors"""
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Add a new doctor"""
        serializer = DoctorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get details of a specific doctor"""
        doctor = get_object_or_404(Doctor, id=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Update doctor details"""
        doctor = get_object_or_404(Doctor, id=pk, user=request.user)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """Delete a doctor record"""
        doctor = get_object_or_404(Doctor, id=pk, user=request.user)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)