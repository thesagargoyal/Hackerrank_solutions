p = int(input())
q = int(input())
ls=[]
for i in range(p,q+1):
    sq=i**2
    s=str(sq)
    d=len(str(i))
    r=s[len(str(sq))-d::]
    l=s[0:len(str(sq))-d:]
    if l=='':
        l=0
    if (int(r)+int(l)) == i:
            ls.append(i)
#print(ls)
if len(ls)==0:
    print("INVALID RANGE")
for i in ls:
    print(i,end=' ')
    
        
