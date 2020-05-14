nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = []
for _ in range(n):
        grid_item = input()
        a.append(grid_item)
print(a)
l=[]
s=0

for i in range(1,n-1):
    for j in range(1,m-1):
        if a[i][j] == 'G' and a[i-1][j] == 'G'and a[i+1][j] == 'G'and\
           a[i][j-1] == 'G'and a[i][j+1] == 'G':
            l.append((i,j))

if len(l)>=2:s+=25
elif len(l)==1:s+=5
else:s=1

print(s)
    


