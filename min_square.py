def min_square(x,y):
    x1=min(x,y)
    area=x*y
    c=0
    while(area!=0):
        for i in range(x1,0,-1):
            while(area>=i**2):
            
                area-=(i*i)
                c+=1
    return c

k=min_square(5,2)
print(k)

        
            
        
        
    
