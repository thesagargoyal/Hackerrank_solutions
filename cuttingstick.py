n = int(input())
arr = list(map(int, input().rstrip().split()))
l=[]
l.append(len(arr))
n-=1
while(len(arr)):
    
    m=min(arr)
    
   
        
    while(arr.count(m)):
                arr.remove(m)
    for i in range(len(arr)):
            arr[i]-=m
    print(arr)
    if len(arr)>0:
        l.append(len(arr))
print(l)
    

