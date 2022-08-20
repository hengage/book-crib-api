from django.db import models
from django.conf import settings

class BookModel(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    isbn = models.PositiveIntegerField(unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'