from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # view.index라는 view 내부로 연결시킴
]