import math
def mean(arr):
    return sum(arr)/len(arr)
def standdev(n, arr):
    marr = mean(arr)
    fluc = []
    for i in arr:
        fluc.append((i-marr)**2)

    return (sum(fluc)/n)**(1/2)

def pearson(n,arr1,arr2):
    nu=0
    arr1m = mean(arr1)
    arr2m = mean(arr2)
    for i in range(n):
        nu+=(arr1[i]-arr1m)*(arr2[i]-arr2m)
    cov = nu/n
    return cov/(standdev(len(arr1),arr1)*standdev(len(arr2),arr2))


#arr = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
arr1=[10,9.8,8,7.8,7.7,7,6,5,4,2]
arr2 = [200,44,32,24,22,17,15,12,8,4]
N=len(arr1)


print(format(pearson(N,arr1, arr2),'.3f'))
