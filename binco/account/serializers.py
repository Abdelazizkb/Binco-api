
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'email', 'name', 'phone', 'address', 'is_active','users')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password','company')