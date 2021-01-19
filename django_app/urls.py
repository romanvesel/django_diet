"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))a
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from clever_menu.views import ProfileModelAPIView


Router = routers.DefaultRouter()
Router.register('profiles', ProfileModelAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clever_menu.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(Router.urls)),
    path('api/docs/', include_docs_urls(title='Clever menu API')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
]

urlpatterns += staticfiles_urlpatterns()
