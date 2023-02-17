# -*- coding: utf-8 -*-
import pymysql
import sys

client = "192.168.0.100"

#################### Connect to mysql Platform ####################
try:
    mydb = pymysql.Connect(
        user=[CHANGE USER],
        password=[CHANGE PASSWORD],
        host="localhost",
        db="rsyslog",
        charset = 'utf8'
    )
    curs = mydb.cursor()
except pymysql.Error as e:
    print(f"Error connecting to mysql Platform: {e}")
    sys.exit(1)


#################### insert Myauth ####################
sql2 = "truncate Myauth;"
curs.execute(sql2)

log_file = open("/backup/rsyslog/"+client+"/auth.log","r")
logs = log_file.readlines()
for log in logs:
    log = log.rstrip()
    cut = log.split(" ")
    date = cut[0]
    host = cut[1]
    process = cut[3]
    message = ""
    for i in cut[4:]:
        message += i + " "

    sql = "INSERT IGNORE INTO Myauth (date, host, process, message) VALUES (%s, %s, %s, %s)"
    val = (date, host, process, message)
    curs.execute(sql, val)
    mydb.commit()

log_file.close()
print("----------success Myauth----------")


#################### insert Postfix ####################
sql2 = "truncate Postfix;"
curs.execute(sql2)

log_file = open("/backup/rsyslog/"+client+"/postfix.log","r")
logs = log_file.readlines()
for log in logs:
    log = log.rstrip()
    cut = log.split(" ")
    date = cut[0]
    host = cut[1]
    process = cut[2]
    message = ""
    for i in cut[3:]:
        message += i + " "

    sql = "INSERT IGNORE INTO Postfix (date, host, process, message) VALUES (%s, %s, %s, %s)"
    val = (date, host, process, message)
    curs.execute(sql, val)
    mydb.commit()

log_file.close()
print("----------success Postfix----------")


#################### insert Rsyslogd ####################
sql2 = "truncate Rsyslogd;"
curs.execute(sql2)

log_file = open("/backup/rsyslog/"+client+"/rsyslogd.log","r")
logs = log_file.readlines()
for log in logs:
    log = log.rstrip()
    cut = log.split(" ")
    date = cut[0]
    host = cut[1]
    process = cut[2]
    message = ""
    for i in cut[3:]:
        message += i + " "

    sql = "INSERT IGNORE INTO Rsyslogd (date, host, process, message) VALUES (%s, %s, %s, %s)"
    val = (date, host, process, message)
    curs.execute(sql, val)
    mydb.commit()

log_file.close()
print("----------success Rsyslogd----------")


#################### insert Rsyslogd ####################
sql2 = "truncate Systemd;"
curs.execute(sql2)

log_file = open("/backup/rsyslog/"+client+"/systemd.log","r")
logs = log_file.readlines()
for log in logs:
    log = log.rstrip()
    cut = log.split(" ")
    date = cut[0]
    host = cut[1]
    process = cut[2]
    message = ""
    for i in cut[3:]:
        message += i + " "

    sql = "INSERT IGNORE INTO Systemd (date, host, process, message) VALUES (%s, %s, %s, %s)"
    val = (date, host, process, message)
    curs.execute(sql, val)
    mydb.commit()

log_file.close()
print("----------success Systemd----------")


#################### insert Vsftpd ####################
sql2 = "truncate Vsftpd;"
curs.execute(sql2)

log_file = open("/backup/rsyslog/"+client+"/vsftpd.log","r")
logs = log_file.readlines()
for log in logs:
    log = log.rstrip()
    cut = log.split(" ")
    date = cut[0]
    host = cut[1]
    process = cut[3]
    message = ""
    for i in cut[4:]:
        message += i + " "

    sql = "INSERT IGNORE INTO Vsftpd (date, host, process, message) VALUES (%s, %s, %s, %s)"
    val = (date, host, process, message)
    curs.execute(sql, val)
    mydb.commit()

log_file.close()
print("----------success Systemd----------")
