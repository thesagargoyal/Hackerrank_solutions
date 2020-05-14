s=input()
l=[0]*26
flag=0
for i in s:
    l[ord(i)-97]+=1


if len(s)%2!=0:
    if l.count(1)>1:
        print('NO')
        
    else:
        print('YES')
else:
    for i in l:
        if i %2!=0:
            print('NO')
            flag=1
            break
    if flag == 0:
        print('YES')
