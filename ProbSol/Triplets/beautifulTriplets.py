'''
https://www.hackerrank.com/challenges/beautiful-triplets/problem
'''
def beautifulTriplets(d, arr):
    aDic ={}
    for i in arr:
        if i in aDic.keys():
            aDic[i]+=1
        else:
            aDic[i]=1
    
    counter=0
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            continue
        if (arr[i]-d) in aDic.keys() and (arr[i]+d) in aDic.keys():
            counter+= aDic[arr[i]-d]*aDic[arr[i]+d]
    return counter

n,d =7,3

a = '1 2 4 5 7 8 10'
arr = list(map(int, a.split()))
print(beautifulTriplets(d, arr))

