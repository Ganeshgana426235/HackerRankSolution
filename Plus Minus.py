#!/bin/python3
n=int(input())
l=input().split()
l=[int(x) for x in l]
n=p=z=0
le=len(l)
for i in l:
    if i<0:
        n+=1
    elif i==0:
        z+=1
    else:
        p+=1
print('%.6f'%(p/le))
print('%.6f'%(n/le))
print('%.6f'%(z/le))