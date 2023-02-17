from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateformat import DateFormat
from .models import SystemEvents, Myauth, Rsyslogd, Systemd, Postfix, Vsftpd
import os
from django.core.paginator import Paginator  


# @login_required(login_url="common:login")
def index(request):
    rsyslogs = SystemEvents.objects.order_by('-id')[:10]
    context = {'rsyslogs':rsyslogs}
    return render(request, "monitor/index.html", context)

# @login_required(login_url="common:login")
def log(request):
    rsyslogs = SystemEvents.objects.order_by('-id')[:10]
    context = {'rsyslogs':rsyslogs}
    return render(request, "monitor/log.html", context)


# @login_required(login_url="common:login")
def detail(request, data_id):
    # rsyslogs = [i for i in range(1, 25)]  # rsyslog 필드 24개
    # rsyslogs = SystemEvents.objects.filter(id=data_id)
    rsyslogs = SystemEvents.objects.get(id=data_id) # data_id 값만 가져오기
    context = {'rsyslogs':rsyslogs}
    return render(request, "monitor/detail.html", context)


#################### 로그 ####################
today = DateFormat(datetime.now()).format('Y-m-d')

#@login_required(login_url="common:login")
def auth(request):
    auth_log = Myauth.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(auth_log, 10) # 한 페이지 당 로그 10개
    page_obj = paginator.get_page(page)
    context = {'auth_log': auth_log, 'page_obj': page_obj}
    return render(request, "monitor/logs/auth.html", context)

#@login_required(login_url="common:login")
def rsyslogd(request):
    rsyslogd_log = Rsyslogd.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(rsyslogd_log, 10)
    page_obj = paginator.get_page(page)
    context = {'rsyslogd_log': rsyslogd_log, 'page_obj': page_obj}
    return render(request, "monitor/logs/rsyslogd.html", context)

#@login_required(login_url="common:login")
def systemd(request):
    systemd_log = Systemd.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(systemd_log, 10)
    page_obj = paginator.get_page(page)
    context = {'systemd_log': systemd_log, 'page_obj': page_obj}
    return render(request, "monitor/logs/systemd.html", context)

#@login_required(login_url="common:login")
def postfix(request):
    postfix_log = Postfix.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(postfix_log, 10)
    page_obj = paginator.get_page(page)
    context = {'postfix_log': postfix_log, 'page_obj': page_obj}
    return render(request, "monitor/logs/postfix.html", context)

#@login_required(login_url="common:login")
def vsftpd(request):
    vsftpd_log = Vsftpd.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(vsftpd_log, 10)
    page_obj = paginator.get_page(page)
    context = {'vsftpd_log': vsftpd_log, 'page_obj': page_obj}
    return render(request, "monitor/logs/vsftpd.html", context)

#@login_required(login_url="common:login")
def tripwire(request):
    tripwire_log = Tripwire.objects.all()
    context = {'tripwire_log': tripwire_log}
    return render(request, "monitor/logs/tripwire.html", context)


# @login_required(login_url="common:login")
def todayLog(request, log_name):
    if log_name is "auth": log_name = "Myauth"
    log = log_name.objects.filter(date__startswith=today)
    context = {'log': log}
    return render(request, "monitor/logs/todayLog.html", context)



#################### 디렉터리 ####################
#@login_required(login_url="common:login")
def bakFiles(request):
    path = "/backup/rsync"
    file_list = os.listdir(path)
    tar = [file for file in file_list if file.endswith(".tar.gz")]
    sql = [file for file in file_list if file.endswith(".sql")]
    file_list = tar + sql
    file_list.sort(reverse=True)
    # file_list_tar = [file for file in file_list if file.endswith(".log")]
    context = {'file_list': file_list}
    return render(request, "monitor/bakFiles.html", context)
