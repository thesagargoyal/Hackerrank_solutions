nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
c.sort(reverse=True)
#print(c)
x=0
a=0
count=0
s=0
y=k
z=eval(str(n))
while(count!=z):
 
    
    
    for i in range(a,a+y):
        count+=1
        
        s+=(x+1)*c[i]
    else:
        
        x+=1
        y=n%k
        n=n%k
        a=k
print(s)

