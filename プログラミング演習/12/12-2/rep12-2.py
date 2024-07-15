#rep12-2.py -*- utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import regex as re
import japanize_matplotlib
import csv

def main():
    Tokyo=list()
    Tokushima=list()
    with open('csv/data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0]=="36":
                temp1=[int(row[4]),int(row[6])]
                Tokushima.append(temp1)
            elif row[0]=="13":
                temp2=[int(row[4]),int(row[6])]
                Tokyo.append(temp2)

    x=[]
    y1=[]
    y2=[]
    for item in Tokushima:
        x.append(item[0])
        y1.append(item[1])

    for item in Tokyo:
        y2.append(item[1])

    plt.rcParams["font.family"]="Meiryo"
    plt.rcParams["font.size"]=10
    plt.figure(figsize=[10,7.5])   
    plt.grid(which="major",color="gray",linestyle="-")
    plt.grid(which="minor",color="gray",linestyle="--")
    plt.xlabel('西暦',loc="right")
    plt.ylabel('人数(人)',loc="top")
    plt.title('徳島県の人口変化と東京都の人口変化')
    plt.plot(x,y1,color="red",label="徳島県")
    plt.yscale("log",base=10)
    plt.plot(x,y2,color="blue",label="東京都")
    
    plt.legend()
    plt.savefig("24G2040.png")
    plt.show()


if __name__ == '__main__':
    main()
