from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 
            'gender', 'blood_group', 'phone_number', 'address', 
            'medical_history', 'allergies', 'created_at', 'updated_at'
        ]
    
    def create(self, validated_data):
        # Set the user to the current authenticated user
        user = self.context['request'].user
        patient = Patient.objects.create(user=user, **validated_data)
        return patient