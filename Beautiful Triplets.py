from itertools import combinations

nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
l2=[]

l=list(combinations(arr,3))
print(l)

for i in l:
    if int(i[2]) - int(i[1]) == d and int(i[1]) - int(i[0]) == d :
        l2.append(i)

print(l2)
print(len(l2))
