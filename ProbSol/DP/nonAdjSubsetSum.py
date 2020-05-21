'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.
'''

def maxSubsetSum(arr): # keeps track of max element till now 
    cmax = max(arr[0],arr[1])
    trackMax = [arr[0],cmax]
    for i in range(2,len(arr)):
        cmax = max(cmax, trackMax[i-2]+arr[i])
        cmax = max(cmax, arr[i])
        trackMax.append(cmax) 
        print(trackMax)
    return trackMax[-1]

l ='2 1 5 8 4'

l = list(map(int,l.split()))
print(maxSubsetSum(l))