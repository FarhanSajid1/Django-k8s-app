from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet
from django.contrib.auth.models import User


router = DefaultRouter()
router.register('users',UserViewSet)
router.register('post', PostViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
    # this is the login route for the api authentication
    path('api-auth/', include('rest_framework.urls')),
]
