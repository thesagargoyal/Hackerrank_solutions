a=input()
b=""
c=""
for i in a:
    if i not in b:
        b+=i
#print(b)
    
for i in b:
    if a.count(i)%2==0:
        pass
    else:
        c+=i
if len(c)==0:
    print("Empty String")
else:
    
    print(c)
        
