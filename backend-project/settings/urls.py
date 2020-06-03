from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grocery/', include('grocery.urls')),
    path('users/', include('users.urls')),
]
