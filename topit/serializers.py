from djoser.serializers import UserSerializer
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = (
            "email",
            "username",
        )


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Data
        fields = (
            "id",
            "title",
            "source",
            "props",
            "description",
            "category",
            "video_url",
            "user",
        )
