from django.urls import path
from . import views

app_name = "monitor"
urlpatterns = [
    # path의 기본 경로 /monitor/
    path("", views.index, name="index"),
    path("bakFiles", views.bakFiles, name="bakFiles"),
    path("log", views.log, name="log"),
    path("auth", views.auth, name="auth"),
    path("rsyslogd", views.rsyslogd, name="rsyslogd"),
    path("systemd", views.systemd, name="systemd"),
    path("postfix", views.postfix, name="postfix"),
    path("vsftpd", views.vsftpd, name="vsftpd"),
    path("tripwire", views.tripwire, name="tripwire"),
    path("todayLog/<str:log_name>", views.todayLog, name="todayLog"),
    path("detail/<int:data_id>/", views.detail, name="detail"), #/monitor/detail
    # path("delete/<int:data_id>/", views.delete, name="delete"), #/monitor/delete
    # path("update/<int:data_id>", views.update, name="update"), #/monitor/update
]
