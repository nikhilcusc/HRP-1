def getRanks(n, arr):
    j = arr.copy()
    j.sort()
    rank=[]
    for i in range(n):
        rank.append(j.index(arr[i]))
    return rank
arr1=[10,9.8,8,7,7.7,7.8,6,5,4,2]
#arr3 = [10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 ]
arr2 = [200,44,32,24,22,17,15,12,8,4]
N=len(arr1)

print(getRanks(N,arr1))
print(getRanks(N,arr2))