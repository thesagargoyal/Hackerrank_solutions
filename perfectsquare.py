import math
ab = input().split()
a = int(ab[0])
b = int(ab[1])
c=0

for i in range(a,b+1):
    a1=math.sqrt(i)
    a2=math.ceil(a1)
    if (a2**2)==i:
        c+=1
print(c)
