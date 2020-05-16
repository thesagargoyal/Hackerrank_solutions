s=input()
n=int(input())
c=""
c1=0
if len(s) == 1 and 'a' in s:
    print(n)
else:
    f=n//len(s)
    c1=s.count('a')*f
    r=n%len(s)
    for i in range(r):
        c+=s[i]
   
    print(c.count('a')+c1)
    
