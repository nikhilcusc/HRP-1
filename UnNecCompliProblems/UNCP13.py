'''
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.
'''
def getArrDiff(arr):
    diff  = max(arr) - min(arr)
    return diff
def removeMax(arr,val):
    minArr = min(arr)
    for i in range(len(arr)):
        if arr[i]==minArr:
            arr[i]+=val
    return arr
def equal(arr):
    diff=getArrDiff(arr)
    operations =0
    while diff>1:
        diff = getArrDiff(arr)
        if diff>=5:
            remove=5
        elif diff>=2:
            remove=2
        else:
            remove=1
        arr = removeMax(arr, remove)
        # arr = min(removeMax(arr,2), removeMax(arr,5), removeMax(arr,1), )
        print(arr)
        operations+=1
    return operations


l = '10 7 12'
l='2 2 3 7'
#l='1 1 5'
l = list(map(int,l.split()))

print('Operations: ',equal(l))