'''
Frequency Queries
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''
import collections
def add2Dic(d, val):
    if val in d.keys():
        d[val]+=1
    else:
        d[val]=1
    return d

def removeFromDic(d, val):
    if val in d.keys():
        if d[val]>0:
            d[val]-=1
        else:
            d[val]=0
    return d
'''
def updateFreqDic(d):
    freqDic = {}
    for i in d.values():
        if i in freqDic.keys():
            freqDic[i]+=1
        else:
            freqDic[i]=1
    return freqDic
'''
def updateFreqDic(freqDic, freq, add):
    if freq in freqDic.keys():
        freqDic[freq] += 1*add
    else:
        freqDic[freq] = 1
    return freqDic

def freqQuery(queries):
    D1 = {}
    freqD1={}
    op=[]
    for q in queries:
        print(q, '\t ', D1)
        if q[0]==1:
            D1 = add2Dic(D1, q[1])
            freqD1 = updateFreqDic(freqD1, D1[q[1]], 1)
        if q[0]==2:
            D1 = removeFromDic(D1, q[1])
            if q[1] in D1.keys():
                freqD1 = updateFreqDic(freqD1, D1[q[1]], -1)
        if q[0]==3:
            print('\nDic:',D1,'\nFreqDic: ',freqD1,'\n')
            try:
                f = freqD1[q[1]]
                if f>0:
                    print(1)
                    op.append(1)
                else:
                    print(0)
                    op.append(0)
            except KeyError:
                print(0)
                op.append(0)
    return op

def freqQuery2(q):
    D1= collections.defaultdict(lambda:0)
    freqD1 =  collections.defaultdict(lambda:0)
    #print(D1, freqD1)

    op=[]

    for c, val in q:
        if c==1:
            freqD1[D1[val]] = max(0, freqD1[D1[val]]-1)
            D1[val] +=1
            freqD1[D1[val]] +=1
        elif c==2:
            freqD1[D1[val]] = max(0, freqD1[D1[val]]-1)
            D1[val] -=1
            if D1[val]>0:
                freqD1[D1[val]] +=1
        else:
            if freqD1[val]>0:
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

freqQuery2(q)
'''
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
'''