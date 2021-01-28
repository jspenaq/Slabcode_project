from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from .models import Project, Task

class ProjectSerializers(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = '__all__'

class TaskSerializers(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user