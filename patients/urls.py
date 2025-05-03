from django.urls import path
from .views import PatientViewSet

urlpatterns = [
    path('patients/', PatientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('patients/<int:pk>/', PatientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]