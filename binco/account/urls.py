from django.urls import path,include
from .views import companyCreate,UserList

urlpatterns = [
    path("employees/", UserList.as_view(), name="employees-list"),
    path("create-company/", companyCreate, name="create-company"),
]