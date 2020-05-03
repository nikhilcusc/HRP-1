'''
You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k. 
'''
from collections import defaultdict
def selfTriplets(n):
    return (n*(n-1)*(n-2))//6


from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    for v in arr:
        if v in r3:
            count += r3[v]
        if v in r2:
            r3[v*r] += r2[v]
        r2[v*r] += 1
        print(v, r2 , r3)
    return count



'''
def countTriplets(arr ,r): # still slow
    if len(set(arr))==1:
        n = len(arr)
        return (n*(n-1)*(n-2))//6
    tripNum=0
    for ind in range(len(arr)):
        smallerEle = arr[ind]//r
        largerEle = arr[ind]*r
        countSmall, countLarge = 0, 0
        for ind2 in range(ind,-1,-1):
            if arr[ind2] == smallerEle:
                countSmall+=1
        for ind2 in  range(ind+1, len(arr)):
            if arr[ind2] == largerEle:
                countLarge+=1
        tripNum+=countLarge*countSmall
    
    return tripNum

def countTriplets(arr, r): # take too long
    posDic={}
    for ind in range(len(arr)):
        ele = arr[ind]
        if ele in posDic.keys():
            posDic[ele].append(ind)
        else:
            posDic[ele]=[ind]
    tripNum=0
    print("Position dictionary: ", posDic)
    posDicKeys=posDic.keys()
    def checkLocs1(ele,dic, r):
        numLocs=0
        for f in dic[ele]:
            for s in dic[ele*r]:
                for t in dic[ele*r*r]:
                    if f < s and s < t:
                        numLocs+=1
        return numLocs

    for ele in posDicKeys:
        if (ele in posDicKeys) and (ele*r in posDicKeys) and (ele*r*r in posDicKeys):
            print(ele, checkLocs1(ele, posDic, r),'\n' )
            tripNum+=checkLocs1(ele, posDic, r)

    return tripNum


def countTriplets(arr, r): #annoningly order matters
    countDic={}
    for ele in arr:
        if ele in countDic.keys():
            countDic[ele]+=1
        else:
            countDic[ele]=1
    print (countDic)
    if len(countDic.keys())==1 and r==list(map(int,countDic.keys()))[0]:
            n = countDic[r]
            return (n*(n-1)*(n-2))//6
            
    tripNum=0
    for ele in countDic.keys():
        
        if (ele*r in countDic.keys()) and (ele*r*r in countDic.keys()):
            print('Adding to tripNum',ele,ele*r,ele*r*r,countDic[ele],countDic[ele*r],countDic[ele*r*r])
            tripNum+=countDic[ele]*countDic[ele*r]*countDic[ele*r*r]
        
    return tripNum
'''
l1 =['1 2 2 4']
r=5
#l1=['1 3 9 9 27 81']
#l1=['1 2 1 2 4']
l1 = ['1 5 5 25 125']
#l1 = ['1 1 1 1']

#l1 = ['1 '*10095]
for l in range(len(l1)):
    nlist = list(map(int, l1[l].split()))
    ReturnedInt = countTriplets(nlist, r)
    print('\n List :',nlist,'\n Number of such triplets:',ReturnedInt,'\n')
