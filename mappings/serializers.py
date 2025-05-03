from rest_framework import serializers
from patients.models import Patient
from doctors.models import Doctor
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_date', 'notes', 
                  'created_at', 'updated_at', 'patient_details', 'doctor_details']
        read_only_fields = ['assigned_date', 'created_at', 'updated_at']
    
    def validate(self, data):
        """
        Check that the patient belongs to the current user
        """
        request = self.context.get('request')
        if request and request.user:
            # Validate the patient belongs to the user
            patient_id = data.get('patient').id
            try:
                Patient.objects.get(id=patient_id, user=request.user)
            except Patient.DoesNotExist:
                raise serializers.ValidationError("Patient does not exist or does not belong to you")
        
        # Check if this mapping already exists
        if PatientDoctorMapping.objects.filter(patient=data.get('patient'), doctor=data.get('doctor')).exists():
            raise serializers.ValidationError("This patient is already assigned to this doctor")
        
        return data
    
    def create(self, validated_data):
        # Set the user to the current authenticated user
        user = self.context['request'].user
        mapping = PatientDoctorMapping.objects.create(user=user, **validated_data)
        return mapping