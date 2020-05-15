from itertools import combinations

n,k=list(map(int,input().split()))
s=list(map(int,input().split()))
l=[]
s1=[]

for i in s:
    if i not in s1:
        s1.append(i)
    


for i in range(len(s1),1,-1):
    l.extend(set(combinations(s1,i)))

c=0
for i in l:
    for j in range(len(i)):
        for z in range(j+1,len(i)):
            if (i[j]+i[z])%k == 0:
                c+=1
                break
    if c == 0:
        print(len(i))
        break
            
        
        
    else:
        c=0
             
             
              
              
   
