from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomAuthorManager

class AuthorModel(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomAuthorManager()

    def __str__(self):
        return self.email

