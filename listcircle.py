s=list(input().split(','))
print(s)
b=[]
x=1
count = 1

b.append(s[0])
while count!=len(s):
    for i in s:
        
        if b[-1].endswith(i[0]):
            if i not in b:
                b.append(i)
                count+=1
            
    
        
print(b)        
        
