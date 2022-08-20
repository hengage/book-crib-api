from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .serializers import AuthorSerializer

Author = get_user_model()

class CreateAuthorView(ListCreateAPIView):
    model = Author
    permission_classes = [permissions.AllowAny,]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()

class RetrieveUpdateAuthorView(RetrieveUpdateAPIView):
    model = Author
    permission_classes = [permissions.AllowAny,]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()
