#python3 code 
l=input().split()
l=[int(x) for x in l]
l.sort()
print(sum(l)-l[len(l)-1],end=" ")
print(sum(l)-l[0])