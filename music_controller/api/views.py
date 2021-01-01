from django.shortcuts import render
from django.http import HttpResponse
from . serializers import RoomSerializer
from . models import Room
from rest_framework import routers, serializers, viewsets
from rest_framework import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

# Create your views here.

# def home(request):
#     return HttpResponse('Hello')


class RoomView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer