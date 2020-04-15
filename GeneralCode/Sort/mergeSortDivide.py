def printArr(a,w):
    low=0
    while low+w<=len(a):
        print(a[low:low+w],end='')
        low+=w

    if low<len(a):
        print(a[low],end='')
        low+=1
    print('\n')
    return

def mergeSortDivide1(a):
    w=1#window
    while w<=len(a):
        print('Window : ',w)
        printArr(a,w)
        w*=2
    return

l1 =['3 2 1 4 5 8 7']

nlist = list(map(int, l1[0].split()))
mergeSortDivide1(nlist)