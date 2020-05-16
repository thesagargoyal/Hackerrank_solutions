s=input()
def separateNumbers(s):
    if len(s)==1:
        return 'NO'
    for i in range(1,len(s)//2+1):
        frst=prev=int(s[0:i])
        sub=s[0:i]
        while len(sub)+len(str(int(prev)+1))<=len(s):
            prev=int(prev)+1
            sub=sub+str(prev)
        if sub==s:
            return 'YES '+str(frst)
    return 'NO'

    
r=separateNumbers(s)
print(r)
