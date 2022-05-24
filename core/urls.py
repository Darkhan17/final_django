from django.contrib import admin
from django.urls import path
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from .views import BooksViewSet, JournaltViewSet

urlpatterns = [
    path('token/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('books/', BooksViewSet.as_view({'get': 'list', 'post': 'create'}), name='view books'),
    path('journals/', JournaltViewSet.as_view({'get': 'list', 'post': 'create'}), name='view books'),
    #path('register', RegisterApi.as_view()),
]
























