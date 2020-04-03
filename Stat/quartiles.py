import math
def median(arr):
    print(arr)
    if len(arr)%2:
        return arr[int(len(arr)/2)]
    else:
        return (arr[int(len(arr)/2)]+arr[int(len(arr)/2)-1])/2

def quartiles(n,arr):
    quar=[]
    if n%2:
        quar.append(median(arr[0:int(n/2)]))
        quar.append(arr[int(n/2)])
        quar.append(median(arr[int(n/2)+1:n]))

    else:
        
        quar.append(median(arr[0:int(n/2)]))
        quar.append(median(arr))
        quar.append(median(arr[int(n/2):n]))
    return quar


#arr = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
arr=[3,7,8,5,12,14,21,13]
N=len(arr)
arr.sort()
print("sorted array : ", arr, " \t length : ", len(arr))
print("\nQuartiles : ",quartiles(N,arr))
