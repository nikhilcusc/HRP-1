#divide the array in 3 parts
#first sublist which is smaller than pivot, second equal and third which is larger

def divQuickSort(arr): #uses extra mem
    pivot=arr[0]
    temparr=[]
    for i in range(len(arr)):
        if arr[i]<pivot:
            temparr.insert(0,arr[i])
        else:
            temparr.append(arr[i])
    return temparr

def divQuickSortInP(arr): #inplace
    #pivot index
    pi=0
    pivot = arr[pi]
    for i in range(pi+1,len(arr)):
        if arr[i]<=pivot:
            temp=arr[i]
            for i1 in range(i,pi,-1):
                arr[i1] = arr[i1-1]
            arr[pi] = temp
            #print(temp, arr, pi)
            pi+=1
    print(arr)
    return pi

l1 =['4 5 3 7 2 4']
nlist = list(map(int, l1[0].split()))

print(divQuickSortInP(nlist))