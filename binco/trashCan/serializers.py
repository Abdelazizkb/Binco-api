
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TrashCan
from rest_framework.permissions import IsAuthenticated, AllowAny



class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCan
        fields = ('id', 'quantity', 'size','company','position')