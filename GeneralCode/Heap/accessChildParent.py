import math


def binHeapParentInd(arr,index):
    if index==0:
        print('Root')
        return index
    return math.floor((index-1)/2)

def binHeapChildrenInd(arr,index):
    if 2*index + 2 < len(arr):
        return [2*index + 1, 2*index + 2]
    elif 2*index + 2 == len(arr):
        return [2*index + 1]
    else:
        print("No children")
    return []

def binHeapParent(arr,index):
    if index==0:
        print('Root')
        return arr[index]
    return arr[math.floor((index-1)/2)]

def binHeapChildren(arr,index):
    if 2*index + 2 < len(arr):
        return [arr[2*index + 1], arr[2*index + 2]]
    elif 2*index + 2 == len(arr):
        return [arr[2*index + 1]]
    else:
        print("No children")
    return

l1 ='64 59 876 263 31 9 87 10 926 628 804 598538 972 4 507 576'
nlist = list(map(int, l1.split()))

print('list :', nlist, ' length: ',len(nlist))

ch1=1
ch2=12
p1=6
p2=7

print("Parent of ",nlist[ch1]," which is at index ", ch1 , ": ",binHeapParent(nlist, ch1), " at index: ",binHeapParentInd(nlist, ch1))
print("Parent of ",nlist[ch2]," which is at index ", ch2 , ": ",binHeapParent(nlist, ch2), " at index: ",binHeapParentInd(nlist, ch2))
print("Child of ",nlist[p1]," which is at index ", p1 , ": ",binHeapChildren(nlist, p1), " at index: ",binHeapChildrenInd(nlist, p1))
print("Child of ",nlist[p2]," which is at index ", p2 , ": ",binHeapChildren(nlist, p2), " at index: ",binHeapChildrenInd(nlist, p2))
