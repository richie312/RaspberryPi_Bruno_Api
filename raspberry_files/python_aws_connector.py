# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 07:58:41 2019

@author: Richie
"""

import pymysql
import datetime
import time

host="richie-database.cml5lvgzqjbw.us-east-1.rds.amazonaws.com"
port=3306
dbname="RDS_MySql"
user="richie31"
password="Nirvikalpa!123"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)

cursor = conn.cursor()

"""Insert Data into Raspberry Pi"""

sql_query = "INSERT INTO readings (id,dateofreading, temperature, Humidity) VALUES (%s,%s,%s,%s)"
sql_query_lastRow = "SELECT MAX(id) FROM readings"
cursor.execute(sql_query_lastRow)
ID = cursor.fetchall()

time = datetime.datetime.now()
sql_date_format = time.strftime('%Y-%m-%d %H:%M:%S')


dateofreading = sql_date_format


temperature = 32.22

Humidity = 1.0

val = (ID[0][0]+1,dateofreading, temperature, Humidity)
cursor.execute(sql_query,val)

conn.commit()