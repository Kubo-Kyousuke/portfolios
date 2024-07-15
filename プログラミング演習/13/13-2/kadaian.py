for i in  range(10):
    print(" ","",end="")
    for j in range(9-i,0,-1):
        print(" ","",end="")
    for k in range(i*2-1):
        print("▲","",end="")
    print("")
