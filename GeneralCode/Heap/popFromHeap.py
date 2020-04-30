import math

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

def binHeapParentInd(arr,index):
    if index==0:
        #print('Root')
        return index
    if index==1 or index==2:#Children of root
        return 0
    return index//2

def binHeapChildrenInd(arr,index):
    if 2*index + 2 < len(arr):
        return [2*index + 1, 2*index + 2]
    elif 2*index + 2 == len(arr):
        return [2*index + 1]
    else:
        pass
        #print("No children")
    return []

def binHeapParent(arr,index):
    if index==0:
        #print('Root')
        return arr[index]
    if index==1 or index==2:#Children of root
        return arr[0]
    return arr[index//2]

def binHeapChildren(arr,index):
    if 2*index + 2 < len(arr):
        return [arr[2*index + 1], arr[2*index + 2]]
    elif 2*index + 2 == len(arr):
        return [arr[2*index + 1]]
    else:
        pass
        #print("No children")
    return

def heapifyMax(arr,val):
    if len(arr)==0:
        arr.append(val)
    else:
        arr.append(val)
        valInd = len(arr)-1
        parentInd = binHeapParentInd(arr, valInd) 
        while  val>=arr[parentInd] and valInd>0 and parentInd>0:
                #print("valInd,parentInd",valInd,parentInd,'val',val,'arr[parentInd]',arr[parentInd],'val>=arr[parentInd]',val>=arr[parentInd],val>=arr[parentInd] and valInd>0)
                #child > parent
                #swap this value to parent
                swap(arr,valInd,parentInd)
                #update indices
                valInd = parentInd
                parentInd = binHeapParentInd(arr, valInd)
    return arr

def buildMaxHeap(arr):
    HeapedArr=[]
    for i in arr:
        #print("Adding value : ",i," to the heap ",end=' ')
        HeapedArr=heapifyMax(HeapedArr,i)
        #print(HeapedArr)
    return HeapedArr

def popMaxHeap(arr):
    ele = arr[0]
    
    # replace with last element and remove it
    arr[0] = arr.pop()
    Ind = 0
    val = arr[Ind]
    Children = binHeapChildrenInd(arr,Ind) #for first comparison
    if len(Children)>1:#2 children
        [lChild, rChild] = Children
        while val<arr[lChild] or val<arr[rChild]:
            #print("Debug ",Ind, arr, val)
            val = arr[Ind]
            Children = binHeapChildrenInd(arr,Ind)
            if len(Children)>1:
                [lChild, rChild] = Children
                if val < arr[lChild] or val < arr[rChild]:
                    #find which child is >
                    if arr[rChild]>arr[lChild]:
                        UpInd = rChild
                    else:
                        UpInd = lChild
                    #swap with max(arr[lChild], arr[rChild])
                    swap(arr, Ind, UpInd)
                    Ind=UpInd
            elif len(Children)==1: #Note we will never have left child empty while rchild something
                lChild=Children[0]
                if val < arr[lChild]: 
                    UpInd = lChild
                    #swap with arr[lChild]
                    swap(arr, Ind, UpInd)
                    Ind=UpInd
                return [arr, ele]    
            else: #no children, exit case?
                return [arr, ele]
        return [arr, ele]
    elif len(Children)==1: #Note we will never have left child empty while rchild something
        lChild=Children[0]
        if val < arr[lChild]: 
            UpInd = lChild
            #swap with arr[lChild]
            swap(arr, Ind, UpInd)
            Ind=UpInd
        return [arr, ele]
    else: #no children, exit case?
        return [arr, ele]

'''
#l1 ='64 59 876 263 31 9 87 10 926 628 804 598538 972 507 576'
l1 = '-35 -78 186 312 583 774 754 640 564 -10 2 852 62 7 817 18 778 535 888 651 726 373 766 160 357 202 643 101 831 261 295 195 -42 -45 574 471 865 154 75 568 991 734 904 48 -63 923 976 250 995 157 275 523 406 266 82 609 286 -62'
#l1 = '195 726 295 186 154 -64 991 904 -40 535'

nlist = list(map(int, l1.split()))
print(nlist)
maxHeap = buildMaxHeap(nlist)
print("Building max heap : ",maxHeap)
Rarr = maxHeap.copy()
i=1
while i<len(nlist):
    [Rarr, Val] = popMaxHeap(Rarr)
    #print(i,"\tReturned value: ", Val)
    print('\n',i,"\tReturned value: ", Val, " Returned arr: ",Rarr)
    i+=1
'''