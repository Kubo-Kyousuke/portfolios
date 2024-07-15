#rep11-0.py -*- Cording:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def main():
    x=np.arange(-5,5,0.01)
    y=np.sin(x)

    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    main()
