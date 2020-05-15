nk = input().split()
n = int(nk[0])
k = int(nk[1])
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
#print(contests)
l=[]
s=0
for i in contests:
    s+=i[0]
    if i[1]==1:
        l.append(i[0])

print(s)
l.sort()
print(l)
c=len(l)-k
print(c)
if c==0:
    print(s-2*min(l))
else:
    for i in l:
        if c>0:
            c-=1
            s-=2*i
print(s)
        
