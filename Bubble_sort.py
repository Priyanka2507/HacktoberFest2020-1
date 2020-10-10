def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                 nlist[i+1] , nlist[i] = nlist[i] ,  nlist[i+1]

                    
n = int(input("Enter no. of elements")
nlist = []
for i in range(n):
    nlist.append(int(input())
bubbleSort(nlist)
print(nlist)
