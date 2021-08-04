from django.urls import path,include
from .views import companyCreate

urlpatterns = [
    path("create-company/", companyCreate, name="create-company"),
]