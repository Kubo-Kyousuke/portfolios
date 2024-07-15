#rep11-1.py
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

def main():
    dataframe=pd.read_csv('oita.csv',encoding='utf-8',names=['月','平均気温','日最高','日最低'])
    x=dataframe['月']
    y1=dataframe['平均気温']
    y2=dataframe['日最高']
    y3=dataframe['日最低']

    plt.xlabel('月')
    plt.ylabel('気温(℃)')
    plt.title('大分県の平均気温(30年)')
    plt.xticks(np.arange(0,13,1))
    plt.yticks(np.arange(0,40,5))
    plt.plot(x,y1,label='平均気温')
    plt.plot(x,y2,label='最高気温')
    plt.plot(x,y3,label='最低気温')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()