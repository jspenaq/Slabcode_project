from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from .serializers import ProjectSerializers, UserSerializer
from .models import Project, Task


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/project-list/',
        'Detail': '/project-detail/<str:pk>/',
        'Create': '/project-create/',
        'Update': '/project-update/<str:pk>/',
        'Delete': '/project-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializers(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def projectCreate(request):
    serializer = ProjectSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def projectUpdate(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def projectDelete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response('Project deleted.')