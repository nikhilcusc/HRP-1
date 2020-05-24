from itertools import permutations, combinations
import itertools
def count1s(s):
    counter=0
    for c in s:
        if int(c):
            counter+=1
    return counter

def getUniqPerms(n): 
    uniqList=[]
    for i in (permutations(range(n),2)):
        if i[0]<i[1]:
            uniqList.append(i)
    return (uniqList)

def mergeStr(a,b):
    c = ''
    counter=0
    for i in range(len(a)):
        if int(a[i]) or int(b[i]):
            c+='1'
            counter+=1
        else:
            c+='0'
    return c, counter


def acmTeam(topic):
    perms = combinations(range(len(topic)),2)
    
    tog, togc = 0, 0
    for i in perms:
        print(i)
        counter=0
        bs = str(bin(int(topic[i[0]],2)|int(topic[i[1]],2)))[2:]
        counter = bs[-5:].count('1')
        print(topic[i[0]],topic[i[1]], bs, counter, end='')
        if counter>tog:
            tog = counter
            togc=0
        if counter==tog:
            togc+=1
        print('\t', tog, togc)
    return tog, togc

l=['10101', '11100', '11010', '00101']
l=['11101','10101','11001','10111','10000','01110']
#print(acmTeam(l))
c = itertools.product(range(10,16),range(10,16))
for i in c:
    print(i, i[0]^i[1])