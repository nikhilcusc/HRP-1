def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

def partition(arr, lo, hi): #inplace pivot high
    pivot = arr[hi]
    i=lo
    for j in range(lo, hi+1):
        if arr[j]<pivot:
            swap(arr,i,j)
            i+=1
    swap(arr,i,hi)
    return i

def divQuickSortPar(arr, low, high):
    
    if  high>low:
        pi=partition(arr,low,high) #pivot low
        divQuickSortPar(arr,low, pi-1)
        divQuickSortPar(arr,pi+1, high)

    return arr

def Sort(arr):
    return divQuickSortPar(arr,0,len(arr)-1)