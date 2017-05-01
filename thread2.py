#!/usr/bin/env python

import os
import sys
import time
import subprocess
import socket

def print_stuff():
    
    ping = sys.stdout.readline()
    if "stop" in ping:
        file = open ('{0}'.format(SysFile),'a+')
        file.write("*****END-OF-PSL*****")
        file.close()
        sys.exit()
    
def main():
    
    SysFile = os.path.join(os.getcwd(),"xyz.txt")
    ping = "start"
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('localhost', 5000))
    client_socket.listen(1)
    conn, addr = client_socket.accept()
    print conn
    print addr
    
    while True:
        
        file = open (SysFile,'a+')
        #data = randint(5,15)
        data = "x"
        file.write(str(data))
        file.close()
        time.sleep(0.5)
        
        if "stop" in str(conn):
            file = open (SysFile,'a+')
            file.write(str(conn))
            file.close()
            time.sleep(0.5)
            
        

            
             

    
if __name__ == "__main__":
    sys.exit(main())
