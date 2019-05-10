from django.urls import path, include
from .views import get_hit_count

urlpatterns = [
    path('home/', get_hit_count , name='counter'),
]