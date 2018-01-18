from django.shortcuts import render

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.authentication import TokenAuthentication

from rest_framework import generics

from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Article, Tags

from . import serializers

import random

class ArticleHomeSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class ArticleViewSet(viewsets.ModelViewSet):
    """Article API Viewset."""
    serializer_class = serializers.ArticleSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Article.objects.all().order_by('date_created').reverse()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author__camp_name',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not self.request.user.is_authenticated:
            instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ArticlePublishedList(generics.ListAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author__camp_name', 'tags__label')
    serializer_class = serializers.ArticleSerializer
    
    def get_queryset(self):
        articles = Article.objects.filter(is_published=True)
        if not articles:
            return articles
        return articles.order_by('date_created').reverse()

class TagViewSet(viewsets.ModelViewSet):
    """Tag API Viewset."""
    serializer_class = serializers.TagSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Tags.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('label',)