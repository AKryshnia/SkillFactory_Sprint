"""
URL configuration for FSTR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from DBpereval import views
from DBpereval.views import PerevalAddedViewset
from . import settings

router = routers.DefaultRouter()
router.register(r'pereval', views.PerevalViewset)
router.register(r'user', views.TouristViewset)
router.register(r'coords', views.CoordinatesViewset)
router.register(r'level', views.LevelViewset)
router.register(r'image', views.PerevalImageViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('submitData/', PerevalAddedViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

