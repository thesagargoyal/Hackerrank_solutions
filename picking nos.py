s = input()
t = input()
k = int(input())

c=""
c2=""
for i in  range(len(s)):
    if str(s[:i+1])==str(t[:i+1]):
        print(s[:i+1])
        pass
        
    else:
        
            c=s[i:]
            c2=t[i:]
            print(c)
            
            
            print(c2)
            break
    
if k >=(len(c)+len(c2)):
    print('Yes')
else:print('No')
