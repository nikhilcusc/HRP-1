from sklearn import linear_model
[m,n] = list(map(int,input().split()))
#print(m,n)
xi=[]
for _ in range(n):
    xi.append(list(map(float,input().split())))
x=[]
y=[]
#print(xi)
for _ in range(n):
    #print(_,len(xi)-1,xi[0])
    x.append(list(xi[_][:m]))
    y.append(xi[_][m])
#print(x,y)
q = int(input())
qv=[]
for _ in range(q):
    qv.append(list(map(float,input().split())))
#print(qv)

lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
#print(a,b)
for _ in  range(q):
    nu=0
    for f in range(m):
        nu+=qv[_][f]*b[f]
    print (round(a+ nu,2))
