n=int(input())
l=list(map(int,input().split()))
l.sort()
l1=[]
from itertools import combinations

a=list(combinations(l,2))

a.sort(key=lambda x:abs(x[0]-x[1]))


ad=abs(a[0][0]-a[0][1])


for i in a:
    if ad == abs(i[0]-i[1]):
        l1.append(i[0])
        l1.append(i[1])
print(l1)
        
