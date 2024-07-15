#prg06-01.py

def fibonacci(n):
    assert n>=1,'require n>=1, but {0}'.format(n)
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        n=fibonacci(n-2)+fibonacci(n-1)
        return n
    
def main():
    for i in range(1,10):
        n=fibonacci(i)
        print('fibonacci({0})={1:2d}'.format(i,n))

if __name__=="__main__":
    main()