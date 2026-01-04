#program for Odd & Even num

def oddEven(num):
    print("Odd" if num & 1 else "Even")

def fraction_to_decimal():
    for i in range (1,10):
        print(1/i)

def traversal(seq):
    for i in seq:
        print(i,end="\t")

import time
def loop_till0(num):
    while num+1:
        print(num)
        num=num-1
        time.sleep(1) 

def isPrime(num):
    if num<=1:
        print("invalid")
        return 0
    for i in range (2,int(num**0.5)+1):
        if not(num%i) :
            return 0
    return 1


