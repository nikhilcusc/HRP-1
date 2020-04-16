#This is a bottom up implementation, using extra storage, not in place
def BUmerge(arr,left,right,end,temparr):
    i,j=left, right
    for k in range(left,end):
        if (i<right and (j>=end or arr[i]<=arr[j])):
            temparr[k]=arr[i]
            i+=1
        else:
            temparr[k]=arr[j]
            j+=1
    return

def Sort(arr):
    temparr=arr.copy()
    w=1
    n=len(arr)
    while w<n:
        i=0
        while i<n:
            BUmerge(arr,i,min(i+w,n),min(i+2*w,n),temparr)
            i+=2*w
        arr=temparr.copy()
        w*=2
    return arr