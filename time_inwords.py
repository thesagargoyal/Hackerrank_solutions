h = int(input())
m = int(input())

l=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
if m==0:
    print("{} o' clock".format(l[h]))
elif 1<=m<=30:
    if m<10:
        print("{} minute past {}".format(l[m],l[h]))
    elif m==15:
        print("quarter past {}".format(l[h]))
    elif m>=10 and m<20:
        print("{} minutes past {}".format(l[m],l[h]))
    elif m==20:
        print("twenty minutes past {}".format(l[h]))
    elif m==30:
        print("half past {}".format(l[h]))
    else:
        m-=20
        print("twenty {} minutes past {}".format(l[m],l[h]))
else:
    m1=60-m
    if m1<10:
        print("{} minute to {}".format(l[m1],l[h+1]))
    elif m1==15:
        print("quarter to {}".format(l[h+1]))
    elif m1>=10 and m1<20:
        print("{} minutes to {}".format(l[m1],l[h+1]))
    elif m1==20:
        print("twenty minutes to {}".format(l[h+1]))
    else:
        m1-=20
        print("twenty {} minutes to {}".format(l[m1],l[h+1]))
    

        
        
    
    
