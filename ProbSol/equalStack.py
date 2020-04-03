'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.
'''
def invertDict(dict1):
    invdict = {}
    for k,v in dict1.items():
        if v in invdict.keys():
            invdict[v].append(k)
        else:
            invdict[v]=[k]
    return invdict

def equalStacks(h1,h2,h3):
    mh = [h1,h2,h3] #master list
    print("Master stack :",mh)
    ms = [] #master sum
    #dictionary with sum elements in ms
    md = {} #master dictionary
    for i in range(len(mh)):
        s=0
        templ = []
        h = mh[i].copy()
        print("h",i,h)
        h.reverse()
        print("h",i,h)
        for ele in h:
            s+=ele
            templ.append(s)
            if s in md.keys():
                md[s]+=1
            else:
                md[s]=1
        templ.reverse()
        ms.append(templ)
    print("Master sums stack :",ms,'\n master dictionary : ',md)
    mdv = md.values()
    print("Master dictionary values : ",mdv)
    if max(list(mdv))<=2:
        
        print(0)  #case with no common sums
    else:
        #select one of the values which shows up in all three sum stacks
        imd = invertDict(md) #inverted master dictionary
        ssv = max(imd[3]) # selected sum values
        print('\n SSV : ',ssv,'\n')
        mind = [] #indices with selected max sum value
        mht = [] #master list truncated 
        for i in range(len(mh)):
            #mind.append(ms[i].index(ssv))
            mht.append(mh[i][ms[i].index(ssv):])
        #print("indices with selected max sum value : ",mind)
        print("Updated lists : ", mht)
         
    return
'''
h1=[3, 2, 1, 1,1]
h2=[4, 3, 2]
h3=[1, 1, 4, 1]

h1=[1,3, 2, 1, 1,1]
h2=[4, 3, 1,1]
h3=[8,5]
'''

#testcase 3
h1 = [1,1,1, 1, 2]
h2=[3, 7]
h3=[1, 3, 1]

equalStacks(h1,h2,h3)