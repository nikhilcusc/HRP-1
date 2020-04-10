#divide the array in 3 parts
#first sublist which is smaller than pivot, second equal and third which is larger

def divQuickSort(arr):
    pivot=arr[0]
    temparr=[]
    for i in range(len(arr)):
        if arr[i]<pivot:
            temparr.insert(0,arr[i])
        else:
            temparr.append(arr[i])
    return temparr

l1 =['4 5 3 7 2']
nlist = list(map(int, l1[0].split()))

print(divQuickSort(nlist))