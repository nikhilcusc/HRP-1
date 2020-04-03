def linearRegr(n,arr1,arr2):
    nu=[0,0,0,0] #xy,x,y,x2
    for i in range(n):
        nu[0] += arr1[i]*arr2[i]
        nu[1] += arr1[i]
        nu[2] += arr2[i]
        nu[3] += arr1[i]**2
    print(nu)
    b = n*nu[0]-(nu[1]*nu[2])
    b /=(n*nu[3]-nu[1]**2)

    a = (nu[2]/n) - b*(nu[1]/n)
    return [a,b] 

arr1=list(range(1,6))
arr2=[2,1,4,3,5]
N=len(arr1)
[a,b]=linearRegr(N,arr1,arr2)
print("\nLinear Regression : ",a,b)
