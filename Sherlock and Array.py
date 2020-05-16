n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

for i in range(len(arr)):
    s1=arr[:i]
    s2=arr[i+1:]
   
    if sum(s1) == sum(s2):
        print('YES')
        break
else:
    print('NO')
