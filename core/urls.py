from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name="Index"),
    path('api/gameservers/', views.GameServerList.as_view()),
    path('api/gameservers/<int:id>', views.GameServerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
