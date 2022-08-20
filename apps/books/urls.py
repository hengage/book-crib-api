from django.urls import path

from .views import BookListCreateAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='books')
]