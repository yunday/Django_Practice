from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_board'

urlpatterns=[
    url(r'^$', views.Todo_board.as_view(), name='todo_board'),
    url(r'^insert/$', views.check_post, name='todo_board_insert'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)