#collatz_problem.py
for n in range(1,10001,1):
    print("初期値   ",n)
    while (n!=1):
        if(n%2)==0:
            n=n/2
            print("　　　   ",n)
        else:
            n=3*n+1
            print("　　　   ",n)
    
    print("最終値   ",n)
