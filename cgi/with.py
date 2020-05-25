#!/usr/bin/env python3
import cgi
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "no")
text2 = form.getfirst("TEXT_2", "no")

cursor.execute("SELECT secret FROM my WHERE login='%s' and password = '%s'" % (text1,text2))
text3 = cursor.fetchall()

print("Content-type: text/html\n")
print("Login: {}".format(text1))
print("Password: {}".format(text2))
print("Secret: {}".format(text3))