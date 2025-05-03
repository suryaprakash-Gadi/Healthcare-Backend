from django.urls import path
from .views import PatientDoctorMappingViewSet

urlpatterns = [
    path('mappings/', PatientDoctorMappingViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('mappings/<int:pk>/', PatientDoctorMappingViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
]