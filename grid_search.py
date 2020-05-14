t = int(input())
count=1
x=0
for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])

        C = int(RC[1])

G = []

for _ in range(R):
            G_item = input()
            G.append(G_item)
rc = input().split()
r = int(rc[0])
c = int(rc[1])
P = []
for _ in range(r):
            P_item = input()
            P.append(P_item)

for i in range(len(G)):
    if P[0] in G[i]:
        r1=i
        k=G[i]
        
        break
for i in range(len(k)):
    if k[i:i+c]==P[0]:
        #print(i)
        c1=i
        break
while(r>1):
    #print(count)
    r-=1
    x+=1
    f=G[r1+1]
    #print(x)
    #print(r)
    
    
    
    if f[c1:c+c1]==P[x]:
        
        count+=1
        r1+=1
        
    else:
        print('NO')
        break
if count==len(P):
    print('YES')

        
    
    

