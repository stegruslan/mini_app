from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from profiles.models import User, Post
from profiles.permissions import IsPostOwner
from profiles.serializers import UserSerializer, PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsPostOwner]

    def perform_destroy(self, instance):
        instance.delete()


class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsPostOwner]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
