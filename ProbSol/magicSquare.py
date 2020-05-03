import itertools
from itertools import permutations, combinations
from datetime import datetime, timedelta

def isMagicSquare(square):
    n = len(square)
    d1, d2=[], [] #diagonal 1 and diagonal 2
    for i in range(len(square)):
        d1.append(list(k for k in  square[i])[i])     
    for i in range(len(square)):
        d2.append(square[i][len(square)-1-i])
    '''
    if len(set(d1))<n or len(set(d2))<n:
        print(square, 'Failed diagonal length test')
        return False
    #print("d1: ",d1, "\td2: ",d2)
    '''
    if sum(d2) == sum(d1):
        rowSum, colSum= [], []
        for i in range(n): #get rows
            rowSum.append(sum(square[i]))
        # transpose the sqaure
        squareT = list(zip(*square))
        for i in range(n):
            colSum.append(sum(squareT[i]))
        #print('Diagonal test passed, \n rowSum: ', rowSum, '\t colSum: ',colSum)
        for i in range(n):
            if colSum[i] == sum(d1) and rowSum[i]==sum(d1):
                pass 
            else:
                return False
        return True
    return False
    
def allMagicSquares(n):
    magicSquares=[]

    l = [i for i in range(1,(n**2)+1)]
    
    #generate permuations of 3
    perm2 = permutations(l,n)
    rows=[]
    for i in perm2:
        #print(i)
        rows.append(list(i))
    perm22 = permutations(rows,n)
    for i in perm22:
        allEle = [j for sub in list(i) for j in sub]
        if len(set(allEle))==n**2:

            #print(list(i))
            if isMagicSquare(list(i)):
                #print('Found a magic Square: ',list(i))
                magicSquares.append(list(i))
    return magicSquares

n = 3

#print(allMagicSquares(n))
sq2 = [[8,3,4],[1,5,9],[6,7,2]]
sq = [[1,2,3],[4,5,6],[7,8,9]]
#print(isMagicSquare(sq2))

timeBefore = datetime.now()
###   
ReturnedList = allMagicSquares(n)
###
timeAfter = datetime.now()
print('it took: ', timeAfter - timeBefore, ' to calculate all magic squares where n: ',n)    
#print(ReturnedList)
for i in ReturnedList:
    for j in i:
        print(j)
    print('\n')
