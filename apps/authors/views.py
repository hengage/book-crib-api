from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .serializers import AuthorSerializer

User = get_user_model()
class CreateAuthorView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny,]
    serializer_class = AuthorSerializer