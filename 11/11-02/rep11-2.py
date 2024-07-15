#rep11-2.py -*- utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import regex as re
import os

def main():
    x = []
    file = open(os.getcwd()+'\prefecture.txt',"r")
    for line in file.readlines():
        pref = re.search(r'(\d+)(.+ )(.+)',line)
        x.append(pref[3])
        
    dataframe = pd.read_csv('data.csv',encoding='utf-8',names=['都道府県','人数'])
    
    y = dataframe['人数']
    
    plt.xlabel('都道府県')
    plt.ylabel('人数')
    plt.title('認知情報科学科1年生のアンケートに基づく出身都道府県')
    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.show()



if __name__ == '__main__':
    main()
