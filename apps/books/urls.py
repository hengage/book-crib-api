from django.urls import path

from .views import BookListCreateAPIView, BookRetrieveUpdateAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='books'),
    path('<int:pk>/', BookRetrieveUpdateAPIView.as_view(), name='book')
]