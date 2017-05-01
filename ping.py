#!/usr/bin/env python

import os
import datetime
import time


run = True
while run:
    ping = True
    while ping:
        time.sleep(1)
        target = "10.85.163.72"
        response = os.system("ping %s -c 0" % target)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if response is not 0:
            print("##########FAILED AT %s##########" %st)
            ping = False
        else:
            print("##########SUCCESS AT %s##########" %st)
            
    
    print '##########START AGAIN##########'
    
    ping = True
    while ping:
        time.sleep(1)
        target = "10.85.163.72"
        response = os.system("ping %s -c 0" % target)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if response is not 0:
            print("##########FAILED AT %s##########" %st)
        else:
            print("##########SUCCESS AT %s##########" %st)