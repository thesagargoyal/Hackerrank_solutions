n,d=list(map(int,input().split()))
e=list(map(int,input().split()))
x=0
c=0
if d%2!=0:
    for i in  range(d,n):
        s=e[x:x+d]
        s.sort()
        m=int(s[(d-1)//2])
        #print(e[i],2*m)
        x+=1
        if e[i]>=(2*m):
            c+=1
            
    print(c)
else:
    for i in  range(d,n):
        s=e[x:x+d]
        s.sort()         # sort method  is used to sort a array in python
        m=int((s[(d-1)//2])+(s[d//2]))/2
        x+=1
        #print(e[i],2*m)
        if e[i]>=int(2*m):
            c+=1
    print(c)
        

