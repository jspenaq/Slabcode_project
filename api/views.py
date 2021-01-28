from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializers
from .models import Project, Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/project-list/',
        'Detail View': '/project-detail/<str:pk>/',
        'Create': '/project-create/',
        'Update': '/project-update/<str:pk>/',
        'Delete': '/project-delete/<str:pk>/',
    }

    return Response(api_urls)



