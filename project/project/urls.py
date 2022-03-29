"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import UserInitAPIView, UserFormAPIView
from project.settings import MEDIA_URL, MEDIA_ROOT

# Resource routing
router = routers.DefaultRouter()
router.register(r'init', UserInitAPIView, basename='init')
router.register(r'form', UserFormAPIView, basename='form')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# Add media URLs
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
