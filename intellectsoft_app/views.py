from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from intellectsoft_app.api.serializer import ClientSerializer, RequestSerializer
from intellectsoft_app.models import Client, Request


def logout_request(request):
    logout(request)
    return redirect('/api/v1/auth/login/')


class ClientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RequestViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
