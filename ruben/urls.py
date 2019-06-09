from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('download/', views.download, name="Download game")
]
