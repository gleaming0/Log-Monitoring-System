# Generated by Django 4.1 on 2023-02-07 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myauth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('process', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Myauth',
            },
        ),
        migrations.CreateModel(
            name='Postfix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('process', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Postfix',
            },
        ),
        migrations.CreateModel(
            name='Rsyslogd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('process', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Rsyslogd',
            },
        ),
        migrations.CreateModel(
            name='ssh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=50, null=True)),
                ('Host', models.CharField(max_length=50, null=True)),
                ('Daemon', models.CharField(max_length=50, null=True)),
                ('Message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'ssh',
            },
        ),
        migrations.CreateModel(
            name='Systemd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('process', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Systemd',
            },
        ),
        migrations.CreateModel(
            name='SystemEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.CharField(max_length=1000, null=True)),
                ('ReceivedAt', models.DateTimeField(null=True, verbose_name='ReceivedAt')),
                ('DeviceReportedTime', models.DateTimeField(null=True, verbose_name='DeviceReportedTime')),
                ('Facility', models.IntegerField(default=0, null=True)),
                ('Priority', models.IntegerField(default=0, null=True)),
                ('FromHost', models.CharField(max_length=1000, null=True)),
                ('Message', models.CharField(max_length=1000, null=True)),
                ('NTSeverity', models.IntegerField(default=0, null=True)),
                ('Importance', models.IntegerField(default=0, null=True)),
                ('EventSource', models.CharField(max_length=1000, null=True)),
                ('EventUser', models.CharField(max_length=1000, null=True)),
                ('EventCategory', models.IntegerField(default=0, null=True)),
                ('EventID', models.IntegerField(default=0, null=True)),
                ('EventBinaryData', models.CharField(max_length=1000, null=True)),
                ('MaxAvailable', models.IntegerField(default=0, null=True)),
                ('CurrUsage', models.IntegerField(default=0, null=True)),
                ('MinUsage', models.IntegerField(default=0, null=True)),
                ('MaxUsage', models.IntegerField(default=0, null=True)),
                ('InfoUnitID', models.IntegerField(default=0, null=True)),
                ('SysLogTag', models.CharField(max_length=1000, null=True)),
                ('EventLogType', models.CharField(max_length=1000, null=True)),
                ('GenericFileName', models.CharField(max_length=1000, null=True)),
                ('SystemID', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'SystemEvents',
            },
        ),
        migrations.CreateModel(
            name='SystemEventsProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.systemevents')),
            ],
            options={
                'db_table': 'SystemEventsProperties',
            },
        ),
    ]
