from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import AuthorViewSet, BookViewSet, BorrowingViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowings', BorrowingViewSet)

# Swagger setup
schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API documentation for Library Management System",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoints
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger at /api/
]
