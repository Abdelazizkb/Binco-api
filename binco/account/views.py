from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import Company
import requests
import json

import requests




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
