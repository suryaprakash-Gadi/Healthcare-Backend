from django.db import models
from django.conf import settings


class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    qualification = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    available_days = models.CharField(max_length=255, help_text="Comma separated days, e.g. 'Monday,Tuesday,Wednesday'")
    available_time = models.CharField(max_length=100, help_text="E.g. '9:00 AM - 5:00 PM'")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
    
    class Meta:
        ordering = ['last_name', 'first_name']