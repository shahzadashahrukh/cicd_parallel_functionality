#!/usr/bin/env python


import sys
import time
import subprocess
import socket

def main():
    
    proc = subprocess.Popen(["python", "thread2.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(5)
    
    print "Yayy"
    #proc.communicate("stop")
    #print "Nayy"
    
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    client_socket.send(data)
    client_socket.close()
    
if __name__ == "__main__":
    sys.exit(main())