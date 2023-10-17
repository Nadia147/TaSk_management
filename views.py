from django.shortcuts import render
from rest_framework import generics 
from .serializers import *
from .models import *

#---------------------------
# Create your views here.
#CURD
class Listtask(generics.ListCreateAPIView):
    queryset= task_manage.objects.all()
    serializers_class=task_serializers

class Detailtask(generics.RetrieveUpdateAPIView):
    queryset= task_manage.objects.all()
    serializers_class=task_serializers

class Createtask(generics.CreateAPIView):
    queryset= task_manage.objects.all()
    serializers_class=task_serializers

class Deletetask(generics.DestroyAPIView):
    queryset= task_manage.objects.all()
    serializers_class=task_serializers