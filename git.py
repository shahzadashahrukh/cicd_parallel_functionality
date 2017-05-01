#!/usr/bin/env python


import os
import sys

def main():
    
    a = "One"
    print a
    print a
    print("%s\n" % a)
    print a
    
    y = ['1','2','a']
    for x in y:
        print x.zfill(3)
            


if __name__ == "__main__":
    sys.exit(main())