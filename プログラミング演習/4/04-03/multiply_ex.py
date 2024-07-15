# multiply_ex.py --*--Coding:utf-8-unix --*--

def multiply(a,b,c):
    """3つの引数の積を返す関数"""
    seki=a*b*c
    return seki

if __name__ =="__main__":
    seki=multiply(10,20,30)
    print("10*20*30=",seki)
    print(multiply.__doc__)