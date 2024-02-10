from django.contrib.auth import logout
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from intellectsoft_app.api.serializer import ClientSerializer, RequestSerializer
from intellectsoft_app.models import Client, Request
from rest_framework.filters import OrderingFilter, SearchFilter


def logout_request(request):
    logout(request)
    return redirect('/api/v1/auth/login/')


class ClientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


class RequestViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'status']
    search_fields = ['status', 'body']
