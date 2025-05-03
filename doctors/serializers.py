from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 'first_name', 'last_name', 'gender', 'specialization',
            'license_number', 'qualification', 'experience_years',
            'phone_number', 'email', 'address', 'available_days',
            'available_time', 'created_at', 'updated_at'
        ]
    
    def create(self, validated_data):
        # Set the user to the current authenticated user
        user = self.context['request'].user
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor