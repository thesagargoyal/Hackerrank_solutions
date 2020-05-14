b,n,m=list(map(int,input().split()))
k=list(map(int,input().split()))
d=list(map(int,input().split()))

l=[(i,j) for i in k for j in d]


l.sort(key=lambda x:sum(x),reverse=True)


for i in l:
    if sum(i)<b:
        print(sum(i))
        break
else:
    print(-1)
