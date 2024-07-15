#is_prmie.py

def isprime(x):
   '''素数判定'''
   if x<2:
      return 'error'
   elif x==2:
      return True
   else:
        i=x-1
        while(i!=1):
            if x%i==0:
                return False
            i-=1
        return True

x=input()
prime=isprime(int(x))
print(prime)
