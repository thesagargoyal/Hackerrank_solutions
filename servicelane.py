nt = input().split()
n = int(nt[0])
t = int(nt[1])
l=[]
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
print(cases)
print(n)
for i in range(len(cases)):
    a,b=cases[i]
    l.append(min(width[a:b+1]))
print(l)
