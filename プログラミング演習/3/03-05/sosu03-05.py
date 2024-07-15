#sosu03-05.py
for m in range(3,1000000,2):
    primeFlag=True
    for n in range(2,m):
        if m%n==0:
            primeFlag=False
            break
    if primeFlag == True:
        print(m," ",end="")
        
    
            