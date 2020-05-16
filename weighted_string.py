s=input()
queries_count = int(input())
queries = []
r=[]

for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

l=[]
d=""
for i in s:
    if i not in d:
        d+=i
for i in d:
    if s.count(d)==1:
        l.append(ord(i)-96)
    else:
        k=ord(i)-96
        c=s.count(i)
        while(c):
            c-=1
            l.append(k)
            k+=(ord(i)-96)
            
print(l)
print(queries)
for i in queries:
    if i in l:
        r.append("Yes")
    else:
        r.append("No")
print(r)
            
            
            
            
    

    
