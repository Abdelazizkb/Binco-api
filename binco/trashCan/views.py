from django.shortcuts import render

# Create your views here.
from .serializers import TrashCanSerializer
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView
from .models import TrashCan
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner



class TrashCanCreateAPIView(CreateAPIView):
      permission_classes = [IsAuthenticated ]
      serializer_class = TrashCanSerializer


class TrashCanListAPIView(ListAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = TrashCanSerializer
      queryset = TrashCan.objects.all()
      def list(self, request, *args, **kwargs):
            list = self.request.user.TrashCan_set.all()
            return list