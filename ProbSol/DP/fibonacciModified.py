'''
https://www.hackerrank.com/challenges/fibonacci-modified/problem
'''
def fibonacciModified(t1, t2, n):
    t = [0]*(n+1)
    t[0] = t1
    t[1] = t2
    for i in range(2,n):
        t[i] = t[i-2] + (t[i-1])**2
        print('ele: ',i+1,'\t val:',t[i] ,'\t', t[i-2] ,'\t', (t[i-1])**2)

    return t[n-1]

t1, t2, n = 0, 1, 5
print(fibonacciModified(t1, t2, n))