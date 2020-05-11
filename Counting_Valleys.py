n=int(input())
s=input()
lv=0
v=0
for i in s:
    if i == 'U':lv+=1
    if i == 'D':lv-=1

    if lv==0 and i == 'U':
        v+=1
print(v)
