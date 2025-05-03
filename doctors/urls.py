from django.urls import path
from .views import DoctorViewSet

urlpatterns = [
    path('doctors/', DoctorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('doctors/<int:pk>/', DoctorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]