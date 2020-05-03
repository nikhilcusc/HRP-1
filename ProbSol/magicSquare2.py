'''
You will be given a 3x3 matrix s of integers in the inclusive range 1-9. We can convert any digit a to any other digit b in the range 1-9 at cost of |a-b|. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.
'''

def getAllSquares():
    allMagicSquares=[
    [[2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]],

    [[2, 9, 4],
    [7, 5, 3],
    [6, 1, 8]],

    [[4, 3, 8],
    [9, 5, 1],
    [2, 7, 6]],

    [[4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]],

    [[6, 1, 8],
    [7, 5, 3],
    [2, 9, 4]],

    [[6, 7, 2],
    [1, 5, 9],
    [8, 3, 4]],

    [[8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]],

    [[8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]]]
    return allMagicSquares

def formingMagicSquare(s):
    magicSquares=getAllSquares()
    minDiff=[]
    for magicSquare in magicSquares:
        tempDiff=0
        for ind1 in range( len(s)):
            for ind2 in range(len(s)):
                tempDiff+=abs(magicSquare[ind1][ind2] - s[ind1][ind2])
        minDiff.append(tempDiff)
    return min(minDiff)

s= [[4,8,2],
[4,5,7],
[6,1,6]]

s2=[[4,9,2],
[3,5,7],
[8,1,5]]

print(formingMagicSquare(s2))

