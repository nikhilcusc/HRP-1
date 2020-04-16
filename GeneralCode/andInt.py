#useful in traversing BIT (Binary Indexed Tree)
for i in range(0,21):
    print(i,' & ',-i,' i&-i:',i&-i,'\tParents i-=i&-i',i-(i&-i),'\tChild (next branch) i+=i&-i',i+(i&-i))

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