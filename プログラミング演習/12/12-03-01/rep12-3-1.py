#rep12-3-1.py

alist=list(range(1,30,1))
alist2=["fizz" if item%3==0 else item for item in alist]
print(alist2)