from pykakasi import kakasi
ks=kakasi()
str1="吾輩は猫である。名前はまだ無い。"
str2="世界文化に技術で貢献する"
str3="広く世界に知識を求める好学心を持つ人材の育成"
str4="自ら学び、自ら思索し創造する人材の育成"

list1=ks.convert(str1)
list2=ks.convert(str2)
list3=ks.convert(str3)
list4=ks.convert(str4)

print(str1)
for word in list1:
    print(word["orig"])

print(str2)
for word in list2:
    print(word["orig"])

print(str3)
for word in list3:
    print(word["orig"])

print(str4)
for word in list4:
    print(word["orig"])