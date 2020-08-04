from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'), # view.index라는 view 내부로 연결시킴
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]