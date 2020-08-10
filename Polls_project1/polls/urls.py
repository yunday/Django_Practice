from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    # path('', views.index, name='index'), # view.index라는 view 내부로 연결시킴
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# pk란 db내의 하나의 데이터를 구분할 수 있는 값