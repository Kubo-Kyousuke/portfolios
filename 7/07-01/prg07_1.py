#prg07_1.py
"""
学籍番号:24G2040
氏名:久保 亨介
"""
import re

def where_is_the_place_by_phone_number(phn):
    if re.search('^047-478',phn):
        print(phn+":"+"千葉工大津田沼校舎")
    elif re.search('^047-454',phn):
        print(phn+":"+"千葉工大新習志野校舎")
    else:
        print(phn+":"+"不明")

def main():
    phone_number1=r'047-478-0222'
    phone_number2=r'047-454-9754'
    phone_number3=r'047-451-1151'

    where_is_the_place_by_phone_number(phone_number1)
    where_is_the_place_by_phone_number(phone_number2)
    where_is_the_place_by_phone_number(phone_number3)

if __name__ == "__main__":
    main()