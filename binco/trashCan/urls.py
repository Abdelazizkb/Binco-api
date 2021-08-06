
from django.urls import path,include
from .views import TrashCanViewSet
from rest_framework.routers import DefaultRouter
from .views import activate
router= DefaultRouter()
router.register('',TrashCanViewSet)

urlpatterns = [
    path('',include(router.urls), name="trash"),
    path('activate/<pk>/',activate, name="trash"),
]
