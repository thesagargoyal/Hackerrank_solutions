arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
l=[0]*6
for i in range(1,6):
        l[i]=arr.count(i)
#print(l)
g=[]
m=max(l)
for i in range(len(l)):
    if l[i]==m:
        g.append(i)
#print(g)
print(min(g))
        
