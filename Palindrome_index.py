s=input()
if s == s[::-1]:
    print(-1)
else:
    x=0
    while(x<len(s)):
        str1=s[0:x]
        str2=s[x+1:]
        st=(str1+str2)
        
        if st == st[::-1]:
            print(x)
            break
        x+=1
    else:
        print(-1)
        
