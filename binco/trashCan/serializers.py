
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import TrashCan,Localisation
from rest_framework.permissions import IsAuthenticated, AllowAny

class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'

class TrashCanSerializer(serializers.ModelSerializer):
    position=LocalisationSerializer(many=False)
    class Meta:
        model = TrashCan
        fields = ('id', 'quantity', 'size','company','position')