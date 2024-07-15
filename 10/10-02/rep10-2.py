#rep10-2.py
import os
import pandas as pd
import numpy as np

student_data=[]
result_data=[]

path=os.getcwd()
print("現在のパス",path)
path=os.path.join(path,"2M_3S.csv")
with open(path) as file:
    student_data=pd.read_csv(path,header=None)

array=student_data.select_dtypes("number").to_numpy()

def hensati(point,ave,hensa):
    hensati=10*(point-ave)/hensa+50
    return hensati

ave=np.average(np.sum(array,axis=1))
print("科目毎の平均点",ave)

variance=np.var(np.sum(array,axis=1))
print("科目毎の分散",variance)

standard_deviation=np.std(np.sum(array,axis=1))
print("科目毎の標準偏差",standard_deviation)

for i in np.sum(array,axis=1):
    Dev=hensati(i,ave,standard_deviation)
    print("合計点:%3d"%(i))
    print("偏差値:%.2f"%(Dev))