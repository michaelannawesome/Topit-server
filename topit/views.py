from django.shortcuts import render
from rest_framework import generics, filters

from . import models
from . import serializers

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    # class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    # def filter_queryset(self, request, queryset, view):
    #     return queryset.filter(owner=request.user)


class DataList(generics.ListAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer

    # def get_queryset(self):
    #     user= self.request.user
    #     return Data.objects.filter(?????????=user)


class DataDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["category", "title", "source", "props"]


class DataCreate(generics.CreateAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer