#!/bin/python3
n=int(input())
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for m in range(i+1):
        print("#",end="")
    print("")