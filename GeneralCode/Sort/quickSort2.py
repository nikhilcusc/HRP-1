#partitioning


def divQuickSortInP(arr,low,high): #inplace, pivot low, maybe has more swaps
    #pivot index
    pi=low
    pivot = arr[pi]
    for i in range(pi+1,high+1):
        if arr[i]<=pivot:
            temp=arr[i]
            for i1 in range(i,pi,-1):
                arr[i1] = arr[i1-1]
            arr[pi] = temp
            #print(temp, arr, pi)
            pi+=1
    return pi

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
        #print('0','low',low,'high', high)
        
        pi=divQuickSortInP(arr,low,high) #pivot low
        #pi=partition(arr,low,high) #pivot high


        #print('1','low',low,'high', high, 'pi',pi)
        divQuickSortPar(arr,low, pi-1)
        print('2','low',low,'high', high, 'pi',pi)
        divQuickSortPar(arr,pi+1, high)
        print('3','low',low,'high', high, 'pi',pi)
        
    return arr

l1 =['3 2 1 4']
nlist = list(map(int, l1[0].split()))
print(divQuickSortPar(nlist,0,len(nlist)-1))