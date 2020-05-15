nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
p=1
c=0
for i in arr:
    if i>k:
        f=i//k
        if (f*k)!=(i):
            #print(f,k,i)
            z=f+1
            a=1
            b=k
            #print("page {}".format(p))
            while(z>0):
                z-=1
                
    
                for j in range(a,b+1):
                    if j == p:
                        c+=1
                        #print(a,b,p)
                a+=k
                b+=k
                if b>i:
                    b=i
                p+=1
        else:
            z=f
            a=1
            b=k
            while(z>0):
                z-=1
                
                
                for j in range(a,b+1):
                    if j ==p:
                        c+=1
                        #print(a,b,p)
                a+=k
                b+=k
                p+=1
            
                    
        
        
        
    elif i<=k:
        #print("pg {}".format(p))
        
        for j in range(i+1):
            if p==j:
                c+=1
            #print(p)
        p+=1
print(c)
