from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'gameserver', views.GameServerViewSet)

app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]