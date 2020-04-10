'''
The median of a list of numbers is essentially it's middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, can you find the median?
'''
#straight forward method is to get a sorted list and get the middle element.
# Find n/2th element in selection sort
'''
def findMedian(a):
    n = len(a)
    s=0
    while s<n/2:
        minv=9999
        i=s
        #find the min value in unsorted array
        while i <n:
            if a[i]<minv:
                minv=a[i]
                minInd = i #save the index
            i+=1
        #swap the value at index i with first value in unsorted array
        temp = a[minInd]
        a[minInd] = a[s]
        a[s] = temp 
        s+=1
    print(a)
    return a[int(n/2)]
'''
# run insertion sort n/2 times
# quicksort with center element?

# get max and min of list and find the element closest to (max-min)/2?
#assumes that list has odd number of unique elements
'''
def findMedian(arr):
    minarr = min(arr)
    maxarr = max(arr)
    half = (minarr+maxarr)/2
    mind,mval=0,999999
    for i in range(len(arr)):
        if abs(half-arr[i])<mval:
            mind=i
            mval = abs(half-arr[i])
    return arr[mind]
'''


l = '0 1 2 4 6 5 3'
l=list(map(int,l.split()))
print(findMedian(l))