#sosu03-04.py
for m in range(2,100):
    n=m-1
    while (n!=1):
        if m%n!=0:
            n-=1
        else:
            break  
    if n==1 :
        print(m," ",end="")
        
    
            