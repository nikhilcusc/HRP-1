'''
https://www.hackerrank.com/challenges/sherlock-and-cost/problem

the sum of the absolute difference of consecutive pairs of A is maximized, where elements of A can be anything between 1 and B[element]
'''
'''
def cost(B):
    a = [0]*len(B)
    def addMax(a,b,i):
        a[i] = b[i]
        return 
    def addMin(a,b,i):
        a[i]=1
        return
    def getCost(arr):
        totCost=0
        for i in range(1,len(arr)):
            totCost += abs(arr[i]-arr[i-1])
        return totCost
    if B[0]>B[1]:
        a[0] = B[0]
        offset=1
    else:
        a[0]=1
        offset=0
    for i in range(1,len(B)):
        if (offset+i)%2:
            addMax(a,B,i)
        else:
            addMin(a,B,i)
        print('at i:',i, '\t a:', a, '\t with b',B)   
    cost = getCost(a)
    return cost
'''
def cost(B):
    l,h= 0, 0
    for i in range(1,len(B)):
        l = max(l, B[i-1]-1)
        h = max(l+B[i]-1, h+abs(B[i]-B[i-1]))
    return max(l,h)
b= '10 1 10 1 10'
B = list(map(int, b.split()))

print(cost(B))