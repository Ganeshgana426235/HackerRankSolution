alic=input().split()
bob=input().split()
a=b=0
for i in range(len(alic)):
    if int(alic[i])>int(bob[i]):
        a+=1
    if int(alic[i])<int(bob[i]):
        b+=1
print(a,b)