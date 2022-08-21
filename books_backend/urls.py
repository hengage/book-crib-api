from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Books Backend",
      default_version='v1',
      description="Backend API for books app",
      contact=openapi.Contact(email="henrychizobaudeh@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authors/', include('authors.urls')),
    path('api/books/', include('books.urls')),

      # Schema Documentation
    path('api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
