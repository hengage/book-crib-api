from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import BookModel
from .serializers import BookSerializer

class BookListCreateAPIView(ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
