"""
filename: prg07_2.py
student_number: 24G2040
Name: 久保 亨介
"""

import regex

def is_CIT(kanji):
    """kanjiが千葉工業大学か千葉工大であればTrueを返し、
    そうでなければ、Falseを返す関数を完成させる"""
    if regex.search(kanji,'千葉工業大学'):
        return True
    elif regex.search(kanji,'千葉工大'):
        return True
    return False

def test_is_CIT(kanji):
    if is_CIT(kanji):
        print(kanji,'is Chiba Institute of Technology')
    else:
        print(kanji,'is not CIT')

def main():
    str1 = '千葉工業大学'
    str2 = '千葉工大'
    str3 = 'CIT'
    str4 = '興亜工業大学'

    test_is_CIT(str1)
    test_is_CIT(str2)
    test_is_CIT(str3)
    test_is_CIT(str4)

if __name__ == '__main__':
    main()