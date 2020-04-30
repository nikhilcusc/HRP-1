
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

# from wikipedia
def iLeftChild(node):
    return 2*node+1

def iParent(node):
    return node//2

def siftDown(arr, start, end):
    root= start
    while iLeftChild(root) <= end:
        child = iLeftChild(root)
        swapI = root
        #compare left child
        if arr[swapI]<arr[child]:
            swapI = child
        #compare right child
        if child+1 <= end and arr[swapI] < arr[child+1]:
            swapI = child+1

        if swapI == root: #no sifting done
            return
        
        swap(arr, root, swapI)
        
        root = swapI

def heapify(arr):
    start =  iParent(len(arr)-1) #parent of last node
    while start >= 0:
        siftDown(arr, start, len(arr)-1)
        start-=1

    return arr

def Sort(a):
    a=heapify(a)
    
    end = len(a)-1
    while end>0:
        swap(a, end, 0) #place the largest element at the end of unsorted subarray
        end-=1 #reduce the unsorted subarr window
        siftDown(a,0,end) #fix the heap 
    return a


