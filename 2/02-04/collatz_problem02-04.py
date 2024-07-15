#collatz_problem02-04.py
count=0
max=0
for i in range(1,1000001,1):
    n=i
    #print("初期値   ",n)
    while (n!=1):
        if(n%2)==0:
            n=n/2
            #print("　　　   ",int(n))
            count+=1
        else:
            n=3*n+1
            #print("　　　   ",int(n))
            count+=1   
    if(max<count):
        max=count
        maxn=i
    #print("最終値   ",int(n))
    #print("計算回数  ",count)
    count=0

print("最も計算回数が多かった数字   ",maxn)

print("最大回数   ",max)
