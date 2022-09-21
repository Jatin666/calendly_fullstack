from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import viewsets
from  calapp.serializers import EventSerializer
from calapp.models import Event


# Create your views here.
def index(request):
    return render(request,'index.html')


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

