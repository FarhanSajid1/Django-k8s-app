from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from blog.models import Post
from rest_framework.response import Response
from rest_framework import serializers
from .permissions import IsOwnerOrReadOnly

# Create your views here

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined') # query by date joined
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def delete(self, request):
        '''This limits the deletion to only the posts that the user created
                There is no point in deleting all of the posts!'''
        Post.objects.filter(author=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



    # if you are not the owner the posts will be read only
    permission_classes = (IsOwnerOrReadOnly,)

    # def post(self, request):




