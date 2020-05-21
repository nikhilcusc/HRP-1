'''
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
'''
def getNonZeros(arr):
    counter=0
    for i in arr:
        if i>0:
            counter+=1
    return counter
def getNonZeroMin(arr):
    minVal=max(arr)
    for i in arr:
        if i>0 and i<minVal:
            minVal=i
    return minVal

def cutTheSticks(arr):
    counter=1
    sticks=[getNonZeros(arr)]
    while counter>=1:
        minArr = getNonZeroMin(arr)
        print('Arr',arr, minArr)
        k = [i-minArr for i in arr]
        arr = k
        print(arr, counter)
        counter = getNonZeros(arr)
        sticks.append(counter)
    
    return sticks[:-1]

a = '1 2 3 4 3 3 2 1'
a= list(map(int,a.split()))
print(cutTheSticks(a))