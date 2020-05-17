'''
Given 3 arrays, a,b,c , find number of such triplets which satisfy q>=p,r where p, q, r are elements of array a,b,c.
'''
'''
def combine2(a,b): #O(m*n)
    ab= []
    for e1 in a:
        for e2 in b:
            #if not [e1, e2] in ab:
            #print(ab,'\t', [e1, e2])
            ab.append([e1,e2])
    return ab

def triplets(a, b, c): #O(M*N*q)
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    counter = 0
    ac = combine2(a,c)
    for t in ac:
        for q in b:
            print(t, q)
            if t[0]<=q and t[1]<=q:
                
                counter+=1
    return counter
'''
def triplets(a, b, c):#O(max(M*N,N*Q))
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort() 
    b.sort()
    c.sort()
    print(a,b,c)
    adic, cdic ={}, {} # will store number of elements <= based on current ele in b
    #create dictionary for a
    for q in b:
        counter, ind =0, 0
        e= a[ind]
        while ind<len(a) and e<=q:
            counter+=1
            ind+=1
            if ind<len(a):
                e=a[ind]
        adic[q]=counter
    #create dictionary for c
    for q in b:
        counter, ind =0, 0
        e= c[ind]
        while ind<len(c) and e<=q:
            counter+=1
            ind+=1
            if ind<len(c):
                e=c[ind]
        cdic[q]=counter
    print('aDic:',adic, '\ncDic:',cdic)
    counter=0
    for q in b:
        counter+=adic[q]*cdic[q]
    return counter
def getUniqueEle(a):
    noDup = []
    for i in a:
        if not i in noDup:
            noDup.append(i)
    return noDup
def triplets(a, b, c): #O(max(M*N,N*Q))
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    a.sort() 
    b.sort()
    c.sort()
    print(a,b,c)
    acounter, ccounter, tc = 0, 0, 0
    bcounter = 0
    while bcounter < len(b):
        q=b[bcounter]
        while acounter<len(a) and a[acounter]<=q:
            acounter+=1
        while ccounter<len(c) and c[ccounter]<=q:
            ccounter+=1
        bcounter+=1
        tc += acounter*ccounter

a ='1 4 5'
b= '2 3 3'
c= '1 2 3'

a =  list(map(int, a.split()))
b = list(map(int, b.split()))
c=  list(map(int, c.split()))

tripletsCount = triplets(a,b,c)
print(tripletsCount)