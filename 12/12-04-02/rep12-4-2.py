#rep12-4-2.py

myDict={"CIT":"Chiba Institute of Technology","CIS":"Congnitive and Information Sciences"}
myDict["CS"]="Computer Science"
myDict["AI"]="Advanced Information science"
myDict.pop("CIT")

for list in myDict:
    print(myDict[list],list,sep=":")