def swapFileData():
     fileName1=input("What would you like to read?:")

     file=open(fileName1,'r','w')
     for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
swapFileData()   