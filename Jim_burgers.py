n = int(input())
orders = []
for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
print(orders)
l=[]

for i in range(len(orders)):
    l.append((i+1,sum(orders[i])))
    
   
#print(l)
def apna(f):
    return(f[1])
l.sort(key=apna)
#print(l)
l1=[i[0] for i in l]
print(l1)
