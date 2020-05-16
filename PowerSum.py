import math
from itertools import combinations

X = int(input())
N = int(input())
c=int(math.sqrt(X))
l=[]
for i in range(1,c+1):
    l.append(i**N)

a=[]
for i in range(1,c+1):
    a.extend(set(combinations(l,i)))


c=0
for i in a:
    if sum(i) == X:
        c+=1
print(c)
