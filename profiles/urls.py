from django.urls import path
from profiles.views import ProfileViewSet

urlpatterns = [
    path('', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile-list'),
    path('<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='profile-detail'),
]
