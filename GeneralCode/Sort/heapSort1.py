import GeneralCode.Heap.popFromHeap as HEAP

def heapS(arr): #this stores the sorted array in another Something does not work with last list 
    endInd = len(arr)
    arr =  HEAP.buildMaxHeap(arr)
    SortedL=[]
    while endInd>1:
        [a, maxEle] = HEAP.popMaxHeap(arr)
        #print(a, maxEle)
        #SortedL.append(maxEle) 
        #Note: we will have max element here 
        SortedL.insert(0,maxEle)
        arr=a.copy()
        endInd-=1
    SortedL.insert(0,a[0])#last values from the heap
    return SortedL
def Sort(a):
    a=heapS(a)
    return a