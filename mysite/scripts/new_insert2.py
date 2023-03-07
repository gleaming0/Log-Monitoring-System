# -*- coding: utf-8 -*-
import pymysql
import sys
from datetime import datetime, date, timedelta

client = "192.168.0.100"


## 어제 날짜 계산
today = date.today().strftime('%Y-%m-%d')
yesterday = (date.today()-timedelta(1)).strftime('%Y-%m-%d')

print("[*] Start Backup " + today + "\n")


#################### Connect to mysql Platform ####################
try:
    mydb = pymysql.Connect(
        user="root",
        password="123456",
        host="localhost",
        db="rsyslog",
        charset = 'utf8'
    )
    curs = mydb.cursor()
except pymysql.Error as e:
    print(f"Error connecting to mysql Platform: {e}")
    sys.exit(1)


#################### Insert Myauth ####################
print("\n[+] Start Myauth")
try:
    log_file = open("/backup/rsyslog/"+client+"/auth.log","r")
except:
    print("[-] Not exists file auth.log")
else:
    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]

        if yesterday not in date:
            continue

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
    print("[*] Success Myauth")


#################### Insert Postfix ####################
print("\n[+] Start Postfix")
try:
    log_file = open("/backup/rsyslog/"+client+"/postfix.log","r")
except:
    print("[-] Not exists file postfix.log")
else:
    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]

        if yesterday not in date:
            continue

        host = cut[1]
        process = cut[2]
        message = " "
        for i in cut[3:]:
            message += i + " "

        sql = "INSERT IGNORE INTO Postfix (date, host, process, message) VALUES (%s, %s, %s, %s)"
        val = (date, host, process, message)
        curs.execute(sql, val)
        mydb.commit()

    log_file.close()
    print("[*] Success Postfix")



#################### Insert Rsyslogd ####################
print("\n[+] Start Rsyslogd")
try:
    log_file = open("/backup/rsyslog/"+client+"/rsyslogd.log","r")
except:
    print("[-] Not exists file rsyslogd.log")
else:
    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]

        if yesterday not in date:
            continue

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
    print("[*] Success Rsyslogd")


#################### Insert Sshd ####################
print("\n[+] Start Sshd")
try:
    log_file = open("/backup/rsyslog/"+client+"/sshd.log","r")
except:
    print("[-] Not exists file sshd.log")
else:
    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]

        if yesterday not in date:
            continue

        host = cut[1]
        pid = cut[2]
        message = ""
        for i in cut[3:]:
            message += i + " "

        sql = "INSERT IGNORE INTO Sshd (date, host, pid, message) VALUES (%s, %s, %s, %s)"
        val = (date, host, pid, message)
        curs.execute(sql, val)
        mydb.commit()

    log_file.close()
    print("[*] Success Sshd")

#################### Insert Vsftpd ####################
print("\n[+] Start Vsftpd")
try:
    log_file = open("/backup/rsyslog/"+client+"/vsftpd.log","r")
except:
    print("[-] Not exists file vsftpd.log")
else:
    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]

        if yesterday not in date:
            continue

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
    print("[*] Success Vsftpd")
