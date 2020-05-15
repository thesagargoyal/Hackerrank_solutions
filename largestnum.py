s=list(input().split(','))
def apna_fun(n):
    return(ord(n[0]))

s.sort(key=apna_fun,reverse=True)
c="".join(s)
print(c)

