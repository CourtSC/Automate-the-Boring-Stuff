tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tList):
    colWidths = [0] * len(tList)
    for index, item in enumerate(tList):
        for i in item:
            if colWidths[index] < len(i):
                colWidths[index] = len(i)
    for j in range(4):
        for k in tList:
            print(k[j].rjust(max(colWidths)), end='')
        print('\n')
    
printTable(tableData)