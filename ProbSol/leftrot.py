def leftRotations(n,arr,d):
    for _ in range(d):
        i = arr.pop(0)
        arr.append(i) 
    return arr

arr=[3,7,8,5,12,14,21,13]
N=len(arr)
d=4
lrot = leftRotations(N,arr,d)
print("\nQuartiles : ",lrot)
