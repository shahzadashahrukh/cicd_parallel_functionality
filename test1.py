#!/usr/bin/env python

import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        return a

def main():
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-v", "--verbose", action = "store_true")
    group.add_argument("-q", "--quiet", action = "store_true")
    
    parser.add_argument('-n', '--num', help = "The Fabonacci number " + \
                        "you wish to calculate", type = int)
    
    parser.add_argument("-o", "--output", help = "Output the " + \
                        "result to a file", action = "store_true")
    
    parser.add_argument("-a", "--abc", help = "Checking " + \
                        "Default", default = 0, action = "store_true")

    parser.add_argument("-d", "--dest", help = "Checking " + \
                        "Default", dest = 'xyz')
    
    args = parser.parse_args()
    result = fib(args.num)
    
    if args.verbose:
        print "For "+str(args.num)+" the fib number is "+str(result)
            
    elif args.quiet:
        print result
    else:
        print "Specify Verbose or Quiet"
    
    if args.output:
        print "saved to file"
    
    if args.abc == 0:
        print "Default == 0"

    elif args.abc < 0:
        print "Default < 0"

    else:
        print "Default > 0"        
        
    print "xyz "+ str(args.xyz)
    
if __name__ == '__main__':
    main()
    