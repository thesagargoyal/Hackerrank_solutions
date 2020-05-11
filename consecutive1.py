n=int(input())
b=bin(n)[2:]
d=[]
str=""
for i in b:
    if i == '1':
        str+=i
    else:
        d.append(str)
        str=""
#print(d)
d.sort(key=len,reverse=True)
print(len(d[0]))
