'''
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.
'''
''' the following approad uses min element as an anchor to bring down other elements.
From a post on https://stackoverflow.com/questions/37797031/unable-to-understand-algorithm
we see that this might not be an optimal solution.
def getArrDiff(arr):
    diff  = max(arr) - min(arr)
    return diff
def getMinArrDiff(arr):
    minArr = min(arr)
    secMinArr = max(arr)
    for i in arr:
        if i>minArr and i<secMinArr:
            secMinArr = i
    print(secMinArr , minArr,secMinArr - minArr)
    return secMinArr - minArr
def upMin(arr,val):
    minArr = min(arr)
    for i in range(len(arr)):
        if arr[i]==minArr:
            arr[i]+=val
    return arr
def removeMax(arr, val):
    maxArr = max(arr)
    for i in range(len(arr)):
        if arr[i]==maxArr:
            arr[i]-=val
    return arr
def equal(arr):
    diff=getArrDiff(arr)
    print(diff)
    operations =0
    
    while diff>=1:
        if diff>=5:
            remove=5
        elif diff>=2:
            remove=2
        else:
            remove=1
        arr = removeMax(arr, remove)
        # arr = min(removeMax(arr,2), removeMax(arr,5), removeMax(arr,1), )
        diff = getArrDiff(arr)
        
        print(arr, diff)
        operations+=1
    
    return operations
'''
# from https://github.com/BlakeBrown/HackerRank-Solutions/blob/master/Algorithms/Dynamic%20Programming/Equal%20-%20O(n)%20greedy.cpp

def numOps(n):
    res = n//5 + (n%5)//2 + (n%5)%2
    return res
def equal(arr):
    sN = min(arr) #smallest number
    ans = 9999
    for i in range(5):
        tempAns = 0
        for e in arr:
            tempAns += numOps(e-sN+i)
        if tempAns < ans:
            ans = tempAns
    return ans

l = '10 7 12'
l='2 2 3 7'
#l='1 1 5'
l = list(map(int,l.split()))

print('Operations: ',equal(l))