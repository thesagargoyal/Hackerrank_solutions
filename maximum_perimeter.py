n = int(input())
sticks = list(map(int, input().rstrip().split()))
l=[]
l1=[]
l2=[]
l3=[]
for i in range(n):
    for  j in range(i+1,n):
        for k in range(j+1,n):
            if sticks[i]+sticks[j]>sticks[k]:
                l.append([sticks[i],sticks[j],sticks[k]])
#print(l)
if len(l)==0:
    print(-1)
else:
    for i in l:
        i.sort()
        l3.append(i)
    print(l3)
    for i in l3:
        a=i[0]
        b=i[1]
        c=i[2]
        
        if a+b>c:
            l1.append(i)
    if len(l1)==0:
        print(-1)
    else:
        print(l1)
        def apna(k):
            return(sum(k))
        l1.sort(key=apna)
        l1.sort(reverse=True)
        print(' '.join(map(str, l1[0])))
