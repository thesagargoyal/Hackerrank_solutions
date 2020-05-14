from itertools import combinations



nm = input().split()
n = int(nm[0])
m = int(nm[1])
t= []
l=[]
for _ in range(n):
        topic_item = input()
        t.append(topic_item)

comb= list(combinations(t,2))


for i in comb:
    c=(str((bin((int(i[0],2) | int(i[1],2)))))[2:]).count('1')
    l.append(c)
print(max(l),l.count(max(l)))

    

