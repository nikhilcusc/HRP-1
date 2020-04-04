'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

def miniMaxSum(arr): # with copy time: O(n), space O(n)
    m = 4
    minarr = arr.copy()
    minar2=[]
    maxarr = arr.copy()
    maxar2=[]
    for _ in range(m):
        minar2.append(minarr.pop(minarr.index(min(minarr))))
        maxar2.append(maxarr.pop(maxarr.index(max(maxarr))))
    print(minar2,sum(minar2))
    print(maxar2,sum(maxar2))
    return

arr = [1,2, 3,4, 5]
miniMaxSum(arr)