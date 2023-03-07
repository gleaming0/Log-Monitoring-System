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


#################### Insert Systemd ####################
print("\n[+] Start Systemd")
try:
    log_file = open("/backup/rsyslog/"+client+"/systemd.log","r")
except:
    print("[-] Not exists file systemd.log")
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

        sql = "INSERT IGNORE INTO Systemd (date, host, process, message) VALUES (%s, %s, %s, %s)"
        val = (date, host, process, message)
        curs.execute(sql, val)
        mydb.commit()

    log_file.close()
    print("[*] Success Systemd")
