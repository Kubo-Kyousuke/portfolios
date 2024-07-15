#guess_number.py
import random

ans=random.randint(1,100)
input_int=input("数字を入力してください")
input_int=int(input_int)
while ans!=input_int:
    if input_int<ans:
        print("小さい")
        input_int=input("もう一度数字を入力してください")
        input_int=int(input_int)
    else:
        print("大きい")
        input_int=input("もう一度数字を入力してください")
        input_int=int(input_int)

print("正解")