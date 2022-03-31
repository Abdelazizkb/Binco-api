from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer,UserCreateSerializer
from .models import Company,UserAccount
import requests
import json
from rest_framework.generics import ListAPIView
import requests

class UserList(ListAPIView):
      serializer_class = UserCreateSerializer

      def get_queryset(self):
          company = self.request.user.company
          return UserAccount.objects.filter(company=company)

@api_view(['POST'])
def companyCreate(request):
    company = Company.objects.create(email=request.data["email"],phone=request.data["phone"],address=request.data["address"],name=request.data["name"])

    data = {
        "email": request.data["user_email"],
        "name": request.data["user_name"],
        "password": request.data["password"],
        "re_password": request.data["re_password"],
        "company": company.id
    }

    print(data)

    result = requests.post("http://localhost:8000/auth/users/", data=data)

    django_response = HttpResponse(
        content=result.content,
        status=result.status_code,
        content_type=result.headers['Content-Type']
    )
    return django_response
