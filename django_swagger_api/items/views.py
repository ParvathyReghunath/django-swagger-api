from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import Itemserializer
# Create your views here.


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = Itemserializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Item.objects.all()
    serializer_class =Itemserializer