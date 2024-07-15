#prg06-a.py

def fact(n):
    if n==0:
        return 1
    else:
        n=n*fact(n-1)
        return n
    
def main():
    for i in range(998):
        m=fact(i)
        print(i,"の階乗は",m)
        print(len(str(m)))

if __name__=="__main__":
    main()