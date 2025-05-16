input_str = input("Nhap X, Y: ")
dimensionms=[int(x) for x in input_str.split(',')]
rowNum=dimensionms[0]
colNum=dimensionms[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)