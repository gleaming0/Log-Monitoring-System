from django.db import models


class SystemEvents(models.Model):
    CustomerID = models.CharField(max_length=1000, null=True)
    ReceivedAt = models.DateTimeField('ReceivedAt', null=True)
    DeviceReportedTime = models.DateTimeField('DeviceReportedTime', null=True)
    Facility = models.IntegerField(default=0, null=True)
    Priority = models.IntegerField(default=0, null=True)
    FromHost = models.CharField(max_length=1000, null=True)
    Message = models.CharField(max_length=1000, null=True)
    NTSeverity = models.IntegerField(default=0, null=True)
    Importance = models.IntegerField(default=0, null=True)
    EventSource = models.CharField(max_length=1000, null=True)
    EventUser = models.CharField(max_length=1000, null=True)
    EventCategory = models.IntegerField(default=0, null=True)
    EventID = models.IntegerField(default=0, null=True)
    EventBinaryData = models.CharField(max_length=1000, null=True)
    MaxAvailable = models.IntegerField(default=0, null=True)
    CurrUsage = models.IntegerField(default=0, null=True)
    MinUsage = models.IntegerField(default=0, null=True)
    MaxUsage = models.IntegerField(default=0, null=True)
    InfoUnitID = models.IntegerField(default=0, null=True)
    SysLogTag = models.CharField(max_length=1000, null=True)
    EventLogType = models.CharField(max_length=1000, null=True)
    GenericFileName = models.CharField(max_length=1000, null=True)
    SystemID = models.IntegerField(default=0, null=True)

    class Meta:
        db_table ='SystemEvents'


class SystemEventsProperties(models.Model):
    question = models.ForeignKey(SystemEvents, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        db_table ='SystemEventsProperties'

# PROJECT
class ssh(models.Model):
    Date = models.CharField(max_length=50, null=True)
    Host = models.CharField(max_length=50, null=True)
    Daemon = models.CharField(max_length=50, null=True)
    Message = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table ='ssh'


class Myauth(models.Model):
    date = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table ='Myauth'


class Rsyslogd(models.Model):
    date = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table ='Rsyslogd'


class Systemd(models.Model):
    date = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table ='Systemd'


class Postfix(models.Model):
    date = models.CharField(max_length=100, null=True)
    host =  models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table ='Postfix'

class Vsftpd(models.Model):
    date = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)


    class Meta:
        db_table ='Vsftpd'

class Tripwire(models.Model):
    date = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)
    process = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)


    class Meta:
        db_table ='Tripwire'
