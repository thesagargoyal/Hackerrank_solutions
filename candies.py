n = int(input())
arr = []

for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
#print(arr)
l=[1]*n
for i in range(n-1):
    #print(f"Value of i {i}")
    if arr[i+1]>arr[i]:
        l[i+1]=l[i]+1
        #print(l)
        
    elif arr[i+1]==arr[i]:
        pass
        
        
#print(l)        
if arr[-1]>arr[-2]:
    l[-1]=l[-2]+1
    #print(l)
    
elif arr[-1]==arr[-2]:
    #print(l)
    pass


else:
    l[-2]=l[-1]+1
#print(l)
print(sum(l))
        
