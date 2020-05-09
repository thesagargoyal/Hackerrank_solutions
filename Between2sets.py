n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[-1]
d=b[0]
f=a+b
g=[0]*(d+1)
l=[]
for i in range(c,d+1):
    for j in f:
        if i>j:
            if i%j == 0:
                g[i]+=1
        else:
            if j%i==0:
                g[i]+=1
for i in range(len(g)):
    if g[i] == (m+n):
        l.append(i)
print(len(l))
                


        
