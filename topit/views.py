from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class DataList(generics.ListAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer


class DataDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer