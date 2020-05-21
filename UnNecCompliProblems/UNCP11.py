'''
Frequency Queries
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''
def freqQuery(queries):
    D1 = {}
    op=[]
    for q in queries:
        print(q, '\t ', D1)
        if q[0]==1:
            if q[1] in D1.keys():
                D1[q[1]]+=1
            else:
                D1[q[1]]=1
        if q[0]==2:
            if q[1] in D1.keys():
                D1[q[1]]-=1
            else:
                D1[q[1]]=0
        if q[0]==3:
            if q[1] in D1.values():
                print(1)
                op.append(1) 
            else:
                print(0)
                op.append(0)
    return op

q = [[1, 3], [2, 3],
[3, 2],
[1, 4],
[1, 5],
[1, 5],
[1, 4],
[3, 2],
[2, 4],
[3, 2]]

#freqQuery(q)
def equalizeArray(arr):
    countDic = {}
    for i in arr:
        print(countDic, i)
        if i in countDic.keys():
            countDic[i]+=1
        else:
            countDic[i]=1
    rep = max(countDic.values())
    return len(arr) - rep

l = '3 3 2 1 3'
l = list(map(int, l.split()))
print(equalizeArray(l))