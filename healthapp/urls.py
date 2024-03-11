from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('post/', views.postData),
]