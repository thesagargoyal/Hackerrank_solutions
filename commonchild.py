a=input().split()
b=a[0]
c=a[1]
d=""
f=""
fl=[]
x=min(len(b),len(c))
for i in  b:
    if i in c:
        d+=i
        #if d in c:
            #l=len(d)
print(d)
#print(len(d))
for i in  c:
    if i in d  :
        f+=i

print(f)

x=min(len(d),len(f))-1
for i in range(len(f)+1):
    if d==f:
        fl.append(d)
    elif d[i:i+x] in f:
            #print(a[i:i+x])
            #print (len(a[i:i+x]))
            #print(i,x)
            #flag=1
            fl.append(d[i:i+x])
            
    else:
            x-=1
def apnafun(x):
    return(len(x))
fl.sort(key=len)
#print(fl)
print(len(fl[-1]))
        
            
