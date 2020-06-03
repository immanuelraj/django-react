from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ShopViewSet

app_name = 'grocery'

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)