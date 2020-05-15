s=input()
st=0
k=0
v=""
c=""
for i in s:
    if i in {'A','E','I','O','U'}:
        if i not in v:
            v+=i
    else:
        if i not in c:
            c+=i
#print(v,c)

def counter(x):
    c=0
    k=len(x)
    global s
    for j in range(len(s)):
            if s[j:j+k] == x:
                c+=1
    
    return c
        
def apna_fun(x):
    global s
    l=list(s)
    count=0
    y=1
    i=l.index(x)
    while ((i+y)!=(len(s)+1)):
        
        z=counter(s[i:i+y])
        print(s[i:i+y],z)
        count+=z
        y+=1
    return count
        
for i in v:    
    k+=apna_fun(i)


for i in c:
    st+=apna_fun(i)
    

if st>k:
    print(f"Stuart {st}")
elif k>st:
    print(f"Kevin {k}")
else:
    print("Draw")



