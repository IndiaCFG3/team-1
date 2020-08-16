from rest_framework import serializers
from . models import users,video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields='__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=video
        fields='__all__'