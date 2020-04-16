
def getSum(BITree,index):
    gsum=0
    while index>0:
        gsum+=BITree[index]
        index-=index&(-index)
    return gsum

def updateBIT(BITree,n,index,val):
    while (index<=n):
        BITree[index]+=val
        index+=index&(-index)
    return

def getInvCounter(a):
    n=len(a)
    invCounter=0
    maxElement = max(a) #O(n)
    BIT = [0]*(maxElement+1) #Binary Indexed Tree
    print(BIT)
    for i in range(1,maxElement+1):
        BIT[i]=0
    print(BIT)

    for i in range(n-1,-1,-1):
        print(i,BIT)
        invCounter+=getSum(BIT,a[i]-1) #why arr[i]-1
        updateBIT(BIT,maxElement,a[i],1) 
    return invCounter

l1 =['3 2 1 4']

nlist = list(map(int, l1[0].split()))
print(getInvCounter(nlist))