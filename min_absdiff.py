n = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
c=[(i,j) for i in range(n) for j in range(n) if A[i]==B[j]]
print(c)
l=[]
for i in c:
    if i[0] not in l:
        l.append(i[0])
print(l)
print(len(l)+1)
