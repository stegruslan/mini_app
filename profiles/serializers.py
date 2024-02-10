from profile import Profile
from django.contrib.auth.hashers import make_password
from profiles.models import User
from profiles.models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ("email", "password")


class DeleteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id",)


class ProfileSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "title", "slug", "author", "body", "publish")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user
        return super().create(validated_data)
