'''
def Sort(a):
    i=1
    while i<len(a):
        j=i
        while j>0 and a[j-1] > a[j]:
            temp = a[j-1]
            a[j-1] = a[j]
            a[j] = temp
            j-=1
        i+=1
    return a
'''
def Sort(a):
    i=1
    n=len(a)
    while i<len(a):
        j=i
        print(i-1,'\t',i)
        while a[j-1]>a[j] and j>=0:
            j-=1
        print('Key : ',a[i],' inserting at: ',j, '\t in ',a)
        if n>2:
            j1=n-2
            temp = arr[n-1]
            while arr[j1] > temp and j1>=0:
                arr[j1+1] = arr[j1]
                j1-=1
                print(' '.join(list(map(str, arr))))
            arr[j1+1] = temp
            print(' '.join(list(map(str, arr))))
        elif n==1:  
            return arr
        else: # len(arr) =2
            temp = arr[1]
            arr[1]=arr[0]
            print(' '.join(list(map(str, arr))))
            arr[0] = temp 
            print(' '.join(list(map(str, arr))))
        i+=1
    return a
