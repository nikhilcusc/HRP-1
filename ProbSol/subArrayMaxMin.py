'''
You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as : max(subarr) - min(subarr)
'''

def maxMin(k, arr): #O(nlogn) + O(1) space
    arr.sort()
    minDiff=arr[k-1] - arr[0]
    for i in range(len(arr)-k+1):
        print(arr[i+k-1] , arr[i],'\t',arr[i+k-1] - arr[i] ,'\t minDiff:',minDiff)
        subArrDiff = arr[i+k-1] - arr[i]
        if minDiff > subArrDiff:
            minDiff = subArrDiff
    return minDiff

'''
# def maxMin(k, arr): #O(nlogn) + O(n) space
#     arr.sort()
#     diffArr = []
#     for i in range(len(arr)-k):
#         subArr = arr[i:i+k]
#         print(i,i+k,'\t',subArr)
#         diffArr.append(max(subArr)-min(subArr))
#     print(diffArr)
#     return min(diffArr)

k=4
arr = '1 2 3 4 10 20 30 40 100 200'

arr = list(map(int,arr.split()))

print(maxMin(k, arr))