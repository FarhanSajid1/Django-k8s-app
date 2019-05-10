from django.shortcuts import render
from rest_framework import viewsets
from ..models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    '''This is the viewset for various requests'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
