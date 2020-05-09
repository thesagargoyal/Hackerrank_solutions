n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
sc=[]
c=0
for i in range(len(s)):
    if sum(s[i:i+m:]) == d:
        c+=1
            
print(c)  
    
    
