#rep12-3-2.py

alist=list(range(1,30,1))
alist2=["buzz" if item%5==0 else item for item in alist]
print(alist2)