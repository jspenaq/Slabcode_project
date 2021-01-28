from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from .models import Project, Task

class ProjectSerializers(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = '__all__'
