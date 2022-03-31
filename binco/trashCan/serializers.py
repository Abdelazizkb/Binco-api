
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TrashCan,Localisation
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'

class TrashCanSerializer(serializers.ModelSerializer):
    position=LocalisationSerializer(many=False,allow_null=True)
    class Meta:
        model = TrashCan
        fields = ('id', 'quantity', 'size','company','position')
