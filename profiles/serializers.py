from profile import Profile
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from profiles.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"]
        )
        return super().create(validated_data)

    class Meta:
        model = User
        fields = '__all__'


class CreatedUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    class Meta:
        model = User
        fields = '__all__'
