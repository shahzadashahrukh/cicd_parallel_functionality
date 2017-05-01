#!/usr/bin/env python


import os
import time

os.environ["SocketIP"] = str("10.85.163.71")
print ""
os.environ["SocketIP"] = os.environ["SocketIP"] + " " + (str("10.85.163.73"))
os.environ["SocketIP"] = os.environ["SocketIP"] + " " + (str("10.85.163.74"))
check = str(os.environ["SocketIP"])
print check
print ""

os.environ["SocketIP"] = check
print os.environ["SocketIP"]

check = check.split()
print check
final = []

for line in check:
    if not str("10.85.163.73") in line:
        final.append(line)
 
os.environ["SocketIP"] = " ".join(final)
print os.environ.get("SocketIP", None)

a = "10.85.163.72"
b = "10.85.163.72"

if a != b:
    print "different"
else:
    print "same"


