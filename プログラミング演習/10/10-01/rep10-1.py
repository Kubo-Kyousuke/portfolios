#rep10-1.py
import os
import numpy as np

student_data=[]

def hensati(point,ave,hensa):
    hensati=10*(point-ave)/hensa+50
    return hensati

path=os.getcwd()
print("現在のパス",path)
path=os.path.join(path,"small-data.csv")
with open(path) as file:
    student_data=np.loadtxt(path,delimiter=",",usecols=[1,2,3])

ave=np.average(np.sum(student_data,axis=1))
print("科目毎の平均点",ave)

variance=np.var(np.sum(student_data,axis=1))
print("科目毎の分散",variance)

standard_deviation=np.std(np.sum(student_data,axis=1))
print("科目毎の標準偏差",standard_deviation)

for i in np.sum(student_data,axis=1):
    Dev=hensati(i,ave,standard_deviation)
    print("合計点:%3d"%(i))
    print("偏差値:%.2f"%(Dev))
