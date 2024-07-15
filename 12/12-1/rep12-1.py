#rep12-1.py -*- utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import regex as re

def main():
    x = []
    file = open('prefecture.txt')
    for line in file.readlines():
        pref = re.search(r'(\d+)(.+ )(.+)',line)
        x.append(pref[3])
        
    dataframe = pd.read_csv('data.csv',encoding='utf-8',names=['都道府県','人数'])
    
    y = dataframe['人数']

    plt.rcParams["font.family"]="Meiryo"
    plt.rcParams["font.size"]=10
    plt.figure(figsize=[10,7.5])   
    plt.yscale("log",base=10)
    plt.grid(which="major",color="gray",linestyle="-")
    plt.grid(which="minor",color="gray",linestyle="--")

    plt.xlabel('都道府県',loc="right")
    plt.ylabel('人数',loc="top")
    plt.title('認知情報科学科1年生のアンケートに基づく出身都道府県')
    plt.bar(x,y,color="green")
    plt.xticks(rotation=90)
    plt.savefig("24G2040.png")
    plt.show()



if __name__ == '__main__':
    main()
