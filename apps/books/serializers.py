from rest_framework import serializers

from books.models import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['title', 'isbn', 'author']