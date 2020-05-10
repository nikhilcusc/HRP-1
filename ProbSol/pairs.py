'''
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
'''

def pairs(k, arr):
    countPairs = 0
    for i  in range(len(arr)):
        for j in range(i+1,len(arr) ):
            if abs(arr[i]-arr[j])==k:
                countPairs+=1
    return countPairs

def pairsDic(k, cost): #using dictionary 
    ind = {}
    countPairs = 0
    for i in (cost):
        ind[i]=1
    print(ind)
    for i in cost:
        if i-k in ind.keys():
            countPairs+=1
    return countPairs

def pairsDic2(k, cost): #using dictionary  and exception handling
    ind = {}
    countPairs = 0
    for i in (cost):
        ind[i]=1
    print(ind)
    for i in cost:
        try:
            print(ind[i-k])
            countPairs+=1
        except KeyError:
            continue
    return countPairs


target = 2
arr = '1 5 3 4 2'

arr = list(map(int, arr.split()))

print(pairsDic2(target, arr))