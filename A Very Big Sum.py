#!/bin/python3

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    n=int(input())
    list1=input().split()
    list1=[int(x) for x in list1]
    result = aVeryBigSum(list1)
    print(result)