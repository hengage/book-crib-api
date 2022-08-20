import imp
from django.contrib import admin

from .models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    model = BookModel
    list_display = ['title', 'isbn', 'author']
    ordering = ["title"]
