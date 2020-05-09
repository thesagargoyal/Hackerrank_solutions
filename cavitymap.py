n = int(input())
a = []
l=[]
l1=[]
for _ in range(n):
        grid_item = input()
        a.append(grid_item)
print(a)


for i in range(n):
        if i == 0 or i== n-1:
                l.append(a[i])
        else:
                for j in range(n):
                        if j == 0 or j== n-1:
                                l1.append(a[i][j])
                        else:
                                
                        
                                if a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]\
                                and a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j]:
                                        l1.append('X')
                                else:
                                        l1.append(a[i][j])
                l.append("".join(l1))
                l1=[]
        print(l)
                        
