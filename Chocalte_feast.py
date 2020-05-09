t = int(input())
for t_itr in range(t):
    ncm = input().split()
    n = int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    w=n//c
    s=0
    def wrap(w):
        if w<m:
            return 0
        else:
            wr=w//m
            w=w%m
            return wr+wrap(w+wr)
    r=wrap(n//c)
    print(r+(n//c))
    
            
            
            
          







