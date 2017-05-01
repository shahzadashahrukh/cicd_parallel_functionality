#!/usr/bin/env python


import os
import sys

def main():
    
    status = ['PASS','PASS','FAIL']
    
    f = open("file.txt", "r")
    line = f.readlines()
    f.close()
    toBe= None
    for index,value in enumerate(line):
        toBe = str(status[index]) + str(value)
        
    f = open("file2.txt", "w+")
    f.write(str(toBe))
    f.close()
    


            


if __name__ == "__main__":
    sys.exit(main())