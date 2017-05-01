#!/usr/bin/env python

import os
import sys
import fcntl
import select
    
def main():
    


    fd = sys.stdin.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    
    epoll = select.epoll()
    epoll.register(fd, select.EPOLLIN)
    
    try:
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                data = ""
                while True:
                    l = sys.stdin.read(64)
                    if not l:
                        break
                    data += l
                print(data.upper(), "")
    
    finally:
        epoll.unregister(fd)
        epoll.close()
        

            
    
if __name__ == "__main__":
    sys.exit(main())
