n = int(input())
s=input()
l=0
sp=0
d=0
c=0
u=0
for i in s:
        if i.isdigit():
            d+=1
            continue
        if i.islower():
            l+=1
            #print(i)
            continue
        if i.isupper():
            u+=1
            continue
        else:
            sp+=1
        
        
print(d,l,u,sp)
if d==0:
    c+=1
    n+=1
if l==0:
    c+=1
    n+=1
if u==0:
    c+=1
    n+=1
if sp==0:
    c+=1
    n+=1
if n<6:
    c+=(6-n)

print(c)
