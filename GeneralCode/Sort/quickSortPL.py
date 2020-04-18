
def divQuickSortInP(arr,low,high): #inplace, pivot low
    #pivot index
    pi=low
    pivot = arr[pi]
    for i in range(pi+1,high+1
    ):
        if arr[i]<=pivot:
            temp=arr[i]
            for i1 in range(i,pi,-1):
                arr[i1] = arr[i1-1]
            arr[pi] = temp
            #print(temp, arr, pi)
            pi+=1
    return pi

def divQuickSortPar(arr, low, high):
    
    if  high>low:
        pi=divQuickSortInP(arr,low,high) #pivot low
        divQuickSortPar(arr,low, pi-1)
        divQuickSortPar(arr,pi+1, high)

    return arr

def Sort(arr):
    
    return divQuickSortPar(arr,0,len(arr)-1)