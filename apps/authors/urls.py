from unicodedata import name
from django.urls import path

from .views import CreateAuthorView

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='create-author'),
]
