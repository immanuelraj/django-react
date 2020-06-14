from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'user'

router = DefaultRouter()
router.register(r'vender', VenderViewSet)
# router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('user/', UserAPIView.as_view()),
    # path('password/reset/', PasswordResetView.as_view(), name='reset'),
    # path('vender/create/', CreateVenderView.as_view()),
    # path('customer/create/', CreateCustomerView.as_view()),
]