from django.urls import path
from . import views

urlpatterns = [
    path('download/xlsx', views.test_view),
]