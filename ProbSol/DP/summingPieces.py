'''
https://www.hackerrank.com/challenges/summing-pieces/problem
'''

def getSeries(n):
    l=[2**(n)-1]
    modVal = 10**9+7
    if n%2:
        run=n//2+1
    else:
        run=n//2
    for i in range(1,run):
        val = (2**(n-i-1)) - (2**(i-1))
        #print(i,'\t',val)
        l.append(l[-1]+val)
    return l

def summingPieces(arr):
    n=len(arr)
    # get the contribution list
    gS = (getSeries(n))
    gSlen = len(gS)
    if n%2:
        revgS = list(reversed(gS))
        gS2 = revgS[1:]
    else:
        gS2 = list(reversed(gS))
    [gS.append(s) for s in gS2]
    print('\t',arr,'\n\t',gS)
    totSum=0
    
    for i in range(len(arr)):
        print('Ele: ', arr[i], '\t Contribites : ',gS[i])
        totSum += arr[i]*gS[i]
    # fix the array
        
    return totSum

#a = '4 2 9 10 1'
a = '1 3 6 6 3 1'
a=list(map(int, a.split()))
print(summingPieces(a))