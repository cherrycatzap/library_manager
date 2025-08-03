from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import AuthorViewSet, BookViewSet, BorrowingViewSet  # adjust path if needed
from library.swagger import urlpatterns as swagger_urls  # make sure the path is correct

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowings', BorrowingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include your API endpoints
]

urlpatterns += swagger_urls  # Append Swagger URLs
