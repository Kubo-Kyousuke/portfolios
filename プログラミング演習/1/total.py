#total.py
import os
import statistics

students=[]
hensachi=[]

file = open('2M.dat')

for line in file.readlines():
    num = int(line)
    students.append(num)

file.close()

total=sum(students)
average=total/len(students)
std_score=statistics.pstdev(students)
print("合計: ",total)
print("平均: ",average)
print("標準偏差: ",std_score)

for point in students:
    st=10*((point-average)/std_score)+50
    print("偏差値: ",st)