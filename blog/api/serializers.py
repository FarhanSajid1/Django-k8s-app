from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    '''This shows and creates new models for us!'''

    class Meta:
        model = Post
        fields = ('title','date_posted', 'author') # these are the fields that are shown
