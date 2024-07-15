#estiname_number.py
import random

ans=input("数字を入力してください")
ans=int(ans)
cpu_ans=random.randint(1,100)

print(cpu_ans)

def cpu(x,y):
    '''コンピュータの回答'''
    if y==2:
        number=random.randint(x,100)
        return number
    elif y==1:
        number=random.randint(1,x)
        return number
    
while(True):
    if cpu_ans>ans:
        cpu_ans=cpu(cpu_ans,1)
        print(cpu_ans)
    elif cpu_ans<ans:
        cpu_ans=cpu(cpu_ans,2)
        print(cpu_ans)
    elif cpu_ans==ans:
        break
print("答えは",cpu_ans)


