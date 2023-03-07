# -*- coding: utf-8 -*-
import pymysql
import sys

client = "192.168.0.100"

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
print("[+] Start Myauth")
try:
    log_file = open("/backup/rsyslog/"+client+"/auth.log","r")
except:
    print("[-] Not exists file auth.log")
else:
    sql2 = "truncate Myauth;"
    curs.execute(sql2)

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
print("[*] Success Myauth")


#################### Insert Postfix ####################
print("[+] Start Postfix")
try:
    log_file = open("/backup/rsyslog/"+client+"/postfix.log","r")
except:
    print("[-] Not exists file postfix.log")
else:
    sql2 = "truncate Postfix;"
    curs.execute(sql2)

    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]
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
print("[+] Start Rsyslogd")
try:
    log_file = open("/backup/rsyslog/"+client+"/rsyslogd.log","r")
except:
    print("[-] Not exists file rsyslogd.log")
else:
    sql2 = "truncate Rsyslogd;"
    curs.execute(sql2)

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
print("[*] Success Rsyslogd")


#################### Insert Sshd ####################
print("[+] Start Sshd")
try:
    log_file = open("/backup/rsyslog/"+client+"/sshd.log","r")
except:
    print("[-] Not exists file sshd.log")
else:
    sql2 = "truncate Sshd;"
    curs.execute(sql2)

    logs = log_file.readlines()
    for log in logs:
        log = log.rstrip()
        cut = log.split(" ")
        date = cut[0]
        host = cut[1]
        pid = cut[2]
        process = cut[3]
        message = ""
        for i in cut[4:]:
            message += i + " "

        sql = "INSERT IGNORE INTO Sshd (date, host, pid, message, process) VALUES (%s,%s, %s, %s, %s)"
        val = (date, host, pid, process, message)
        curs.execute(sql, val)
        mydb.commit()

    log_file.close()
print("[*] Success Sshd")


#################### Insert Vsftpd ####################
print("[+] Start Vsftpd")
try:
    log_file = open("/backup/rsyslog/"+client+"/vsftpd.log","r")
except:
    print("[-] Not exists file vsftpd.log")
else:
    sql2 = "truncate Vsftpd;"
    curs.execute(sql2)

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
print("[*] Success Vsftpd")
