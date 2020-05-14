nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
a=eval(str(arr))
arr.sort(reverse=True)
#print(arr)
#print(a)

while(k):
    
    for i in range(n):
        if arr[i]>a[i]:
        
            if k==0:
                break
            else:
                k-=1
                l=a.index(arr[i])
                t=a[i]
                
                a[i]=a[l]
                
                a[l]=t
                #print(a)
                
            
        else:
            pass
    else:
        break
print(a)
            
 
    
