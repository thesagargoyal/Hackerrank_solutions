n=int(input())
a=[int(x) for x in input().strip().split(' ')]

l=[0]*(max(a)-min(a)+1)
print(max(a))
f=[]
for i in a:
    if i not in f:
        f.append(i)
    

for i in f:
    l[i]+=a.count(i)
    
    
print(len(l))
print(*l)
