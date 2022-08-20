from unicodedata import name
from django.urls import path

from .views import CreateAuthorView, RetrieveUpdateAuthorView

urlpatterns = [
    path('', CreateAuthorView.as_view(), name='create-author'),
    path('<int:pk>/', RetrieveUpdateAuthorView.as_view(), name='author'),
]
