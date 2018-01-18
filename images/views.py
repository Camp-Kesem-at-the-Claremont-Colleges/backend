from django.shortcuts import render

from rest_framework import permissions

from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Image
from . import serializers

class ImagesViewSet(viewsets.ModelViewSet):
    """Image API Viewset."""

    serializer_class = serializers.ImageSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Image.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
