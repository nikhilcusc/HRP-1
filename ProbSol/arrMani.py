'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
'''
import numpy as np
import time

def arrayManipulation(n, queries): #basic and slow O(n)
    arr = [0]*n
    for query  in queries:
        runner = query[0]-1
        while runner<query[1]:
            arr[runner]+=query[2]
            runner+=1
        #print("Query was : ",query,"\t arr :", arr)
    return max(arr)

def arrayManipulationNumpy(n, queries): #using numpy
    arr = np.asarray([0]*n)
    for query  in queries:
        arr[query[0]-1:query[1]]+=query[2]
        #print("Query was : ",query,"\t arr :", arr)
    return max(arr)

#step ladder approach
#updates only the end points and makes a note of additions in the first part and differences in the second part
def arrayManipulation2(n, queries): #only change end points O(1) for updates
    arr = [0]*(n+1)
    for query  in queries:
        arr[query[0]-1]+=query[2]
        arr[query[1]]-=query[2]
        print("Query was : ",query,"\t arr :", arr)
    
    x,maxarr=0,0
    for i in ((arr)): #why, because some of the values might go negetive, so to find the max we need to linearly add all the elements and then find the max
        x+=i
        if maxarr<x: maxarr=x
    
    return maxarr


print("in arrMani")

#if __name__=='main':
n = 5 
m = 3
q = [[1,2,100],
[2,5,100],
[3,4,100]]
start = time.time()
print(arrayManipulationNumpy(n,q))
end = time.time()
print("arrayManipulationNumpy : ",end - start)


start = time.time()
print(arrayManipulation(n,q))
end = time.time()
print("arrayManipulation : ",end - start)

start = time.time()
print(arrayManipulation2(n,q))
end = time.time()
print("arrayManipulation2 : ",end - start)