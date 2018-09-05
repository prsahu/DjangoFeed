# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from feedreader.models import Entry
from .serializers import ArticleSerializer
from .viewsets import ArticleViewSet

from django.shortcuts import render

account_list = ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

entry_individual = ArticleViewSet.as_view({
    'get': 'retrieve'
})

# Create your views here.
class ArticleViewSet(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = ArticleSerializer