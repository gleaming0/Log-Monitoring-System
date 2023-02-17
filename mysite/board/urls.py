from django.urls import path
from . import views

urlpatterns = [
    # path의 기본 경로 /board/
    path('', views.index, name='index'),
    # path('detail', views.detail, name='detail'), #/monitor/detail
    # path('delete', views.delete, name='delete'), #/monitor/delete
    # path('update', views.update, name='update'), #/monitor/update
]