t=int(input())
l=input().split()
l=[int(x) for x in l]
c=m=0
for i in l:
    c=l.count(i)
    if m<c:
        m=c
print(m)
