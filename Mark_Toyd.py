nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
prices.sort()
p=len(prices)
l=[]
for i in range(len(prices)):
    if prices[i]>k:
        p=i
        break
l.append(prices[0])
for i in range(1,p):
    if (sum(l)+prices[i])<=k:
        l.append(prices[i])
print(l)
print(len(l))
