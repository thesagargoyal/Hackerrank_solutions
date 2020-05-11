n = int(input().strip())

arr = []

for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
print(arr)

s=0
s1=0
x=n-1
for i in range(n):
    s+=arr[i][i]
    s1+=arr[i][x]
    x-=1
print(abs(s-s1))
