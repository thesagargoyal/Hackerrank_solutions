n = int(input())
g = input().rstrip().split()
h = list(map(int, input().rstrip().split()))
s = int(input())
c=0
f=[]
l=[]
t=[]
d=[]
for s_itr in range(s):
        firstLastd = input().split()
        f.append(int(firstLastd[0]))
        l.append(int(firstLastd[1]))
        d.append( firstLastd[2])

for y in range(len(d)):      
    for i in range(f[y],l[y]+1):
        x=len(g[i])
        for j in range(len(d[y])):
                       if d[y][j:j+x] == g[i]:
                           #print(g[i])
                           #l1.append(g[i])
                           c+=h[i]
        #l2.append(l1)
        #l1=[]
    t.append(c)
    c=0
        
#print(t)
print(min(t),max(t))
#print(l2)
                       
    
