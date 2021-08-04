
from django.urls import path
from .views import TrashCanListAPIView,TrashCanCreateAPIView

urlpatterns = [

    path('list/', TrashCanListAPIView.as_view(), name="trash-list"),
    path('create/', TrashCanCreateAPIView.as_view(), name="create-trash")

]
