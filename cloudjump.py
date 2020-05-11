import time
nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
e=100
flag=0
i=0
while(flag==0):
    
            
            i+=k
            print(i)
            time.sleep(4)
            if i>=n:
                print(i)
                i-=n
                print(i)
            if i==0:
                flag=1
                if c[0]==1:
                    e-=3
                else:
                    e-=1
                
                break
            else:
                if c[i]==1:
                    e-=3
                else:
                    e-=1

print(e)
   
    
             
        


    
    
    
