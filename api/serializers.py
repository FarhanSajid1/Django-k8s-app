from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post



class UserSerializer(serializers.ModelSerializer):

    # creating a urls for the posts, instead of numbers
    # posts lookup field for all the posts
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                read_only=True,
                                                view_name='post-detail'
                                                )
    class Meta:
        model = User
        fields = ('username', 'url', 'posts')


class PostSerializer(serializers.ModelSerializer):
    date_posted = serializers.ReadOnlyField()

    # setting the post author as the default user, and as read only
    author = serializers.HyperlinkedRelatedField(read_only=True, default=serializers.CurrentUserDefault(), view_name='user-detail')
    # author = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('title', 'content', 'date_posted', 'author')



