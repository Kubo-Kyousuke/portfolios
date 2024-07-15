#rep12-3-3.py

alist=list(range(1,30,1))
alist2=["fizz buzz" if item%15==0 else "buzz" if item%5==0 else "fizz" if item%3==0 else item for item in alist]
print(alist2)