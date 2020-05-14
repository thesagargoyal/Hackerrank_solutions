n=int(input())
l=[]
s=str(n)
l.extend(s)
print(l)
c=0
for i in l:
    if int(i)==0:
        pass
    else:
        if n%int(i)==0:
            c+=1
print(c)
