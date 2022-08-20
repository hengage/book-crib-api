from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model
Author = get_user_model()
from books.models import BookModel

class BookInline(admin.TabularInline):
    model = BookModel
    extra = 0

@admin.register(Author)
class CustomUserAdmin(UserAdmin):
    model = Author
    list_display = ['email', 'first_name', 'last_name']

    ordering = ["first_name"]
    inlines = [
        BookInline
    ]

    fieldsets= [
        ("Basic User Details", {
            "fields": ['email', 'first_name', 'last_name',]
        }),

        (
            "User Status (sensitive area, proceed with caution)",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
                "classes": ["collapse"],
            },
        ),

        (
            None,
            {
                "fields": [
                    "last_login",
                ]
            },
        ),

        (None, {"fields": ["groups", "user_permissions"]}),
    ]

    add_fieldsets = (
        (
            "User Personal Details",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                ),
            },
        ),

        (
            "User status",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active"
                ),
            },
        ),
    )