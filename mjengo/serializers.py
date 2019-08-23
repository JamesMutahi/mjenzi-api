from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Materials, Project, Requests


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user', "name", "contractor_email", "password")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.title)
        instance.contractor = validated_data.get("contractor_email", instance.artist)
        instance.contractor = validated_data.get("password", instance.artist)
        instance.save()
        return instance


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ("name", "quantity", 'project')

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.project = validated_data.get("project", instance.project)
        instance.save()
        return instance


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ("name", "quantity", "project", "photo")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.project = validated_data.get("project", instance.project)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
