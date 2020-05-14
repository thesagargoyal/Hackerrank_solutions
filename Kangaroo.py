x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])

while(True):
    if x1==x2:
        print('YES')
        break
    elif x1>x2:
        print('NO')
        break
    elif max(x1,x2)==x2 and max(v1,v2)==v2:
        print('NO')
        break
    else:
        x1+=v1
        x2+=v2
        
