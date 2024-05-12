#!/home/ckw91/venv/bin/python3

import sys
import os
#
import shlex
#
import subprocess
#
import cgi, cgitb

import re
import math

import cx_Oracle

import db_config

cgitb.enable()

os.environ['LD_LIBRARY_PATH'] = '/usr/lib/oracle/21/client64/lib/'
os.environ['ORACLE_HOME'] = '/usr/lib/oracle/21/client64'
os.environ['ORACLE_SID'] = 'csdbora'


# Create instance of FieldStorage
form = cgi.FieldStorage()


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cursor = con.cursor()

cursor.execute("SELECT count(*) from job")
row = cursor.fetchone()
job_num = row[0]

cursor.execute("SELECT count(*) from member")
row = cursor.fetchone()
member_num = row[0]

cursor.execute("SELECT count(*) from c_g")
row = cursor.fetchone()
c_g_num = row[0]

print ("Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<title>DrPengsAIIPDemos Job Search</title>")
print("<meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1'>")
print("")
print("</head>")
print("<body BGCOLOR='#FFFFFF' LINK='#0088ff' ALINK='#FF0000' VLINK='#CC0000'>")
print("<center><h2>DrPengsAIIPDemos Welcomes You! </h2></center>")
print("<center>")
print("<img src='http://newfirebird.cs.txstate.edu/~ckw91/img/background.gif' width='550' height='180'  usemap='#map1' border='0'><map name=map1>")
print("<area shape='rect' coords='3,3,215,180' href='http://newfirebird.cs.txstate.edu/~ckw91/demo/proc/unix-version/html/job_search-py.html'>")
print("<area shape='rect' coords='310,3, 550,180' href='/~ckw911/cgi-bin/employers.pl'>")
print("</map>")

print("<br>")
print("<br>")
print("<center>")
print("<i>")
print("Registered Engineers:", member_num, "<br>")
print("Total jobs:", job_num,"<br>")
print("Total registered college graduates:", c_g_num, "<br>")
print("</i>")
print("</center>")
print("<br>")

print("<br>")
print("<b>")
print("DrPengsAIIPDemos.com, Python version,  will assist and challenge you to be where you can be in the 21th centry in the high tech, high competitive, high reward world.")
print("</b>")
print("<br>")
print("<br>")
print("<br>")
print("<table cellspacing='0' cellpadding='3' border='0'>")
print("<tr>")
print("	<td> <a href='/~ckw91/cgi-bin/home.py'> Home </a>")
print("	<td> <a href='http://newfirebird.cs.txstate.edu/~ckw91/demo/proc/unix-version/html/job_search-py.html'>Job Search </a>")
print("        <td> <a href='http://newfirebird.cs.txstate.edu/~ckw91/demo/proc/unix-version/html/employer_login.html'>Employers </a>")
print("        <td> <a href='http://newfirebird.cs.txstate.edu/~ckw91/demo/proc/unix-version/html/member_login.html'>Members </a>")
print("</tr>")

print("</table>")
print("</center>")
print("")
print("")
print("<br>")
print("	<i>Copyright @2023 DrPengsAIIPDemos.com Inc. All rights reserved.")
print("	</i>")
print("</body>")
print("</html>")
