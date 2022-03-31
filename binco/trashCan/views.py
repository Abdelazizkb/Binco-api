import json

from django.shortcuts import render

# Create your views here.
from .serializers import TrashCanSerializer
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView
from rest_framework import viewsets
import requests

from .models import TrashCan,Localisation
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.decorators import api_view
from django.http import HttpResponse




class TrashCanViewSet(viewsets.ModelViewSet):
      serializer_class = TrashCanSerializer
      queryset = TrashCan.objects.all()
      lookup_field = 'id'

      def get_queryset(self):
          if(self.request.user.is_authenticated) :
            company = self.request.user.company
            return TrashCan.objects.filter(company=company)
          else :
            return []
      def perform_create(self, serializer):
          company=self.request.user.company
          serializer.save(company=company)






@api_view(['post'])
def activate(request,pk):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    geoloc = Localisation.objects.create(lat=body['lat'], lng=body['lng'])

    trash = TrashCan.objects.get(id=pk)
    trash.position = geoloc
    trash.save()

    result = requests.get("http://localhost:8000/trash/"+pk+"/")

    django_response = HttpResponse(
              content=result.content,
              status=result.status_code,
              content_type=result.headers['Content-Type']
    )
    return django_response






