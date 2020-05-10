'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a cost. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.
'''

def binSearchMod(list1, value, start, end): #implemented for descending order
    mid = (start+end)//2
    #print('Looking for value: ', value, ' in ', start, end, mid , 'list :', list1)
    #conditions for element at start or end or mid
    if value==list1[start]:
        mid = start
    if value == list1[end]:
        mid = end
    if value == list1[mid]:
        return [True, mid]    
    if end-start == 1: # if some element lies in between 2 numbers of array
        #print('Found between ', start, end)
        return [False, start]
    if value < list1[mid]:
        return binSearchMod(list1, value, mid, end)
    else:
        return binSearchMod(list1, value, start, mid)
'''
def findIndex(arr, val): 
    occ = [i for i, v  in enumerate(arr) if v==val]
    
    if len(occ)==0:
        return False
    return occ

def whatFlavors(cost, money): #basic solution with linear search
    fInd = [] #flavour indices
    for i, v in enumerate(cost):
        if v < money:
            occ = findIndex(cost, money-v)
            fInd.append(i+1)
            
            if occ:
                if len(occ)==1:
                    fInd.append(occ[0]+1)
                    if i == occ[0]: # same element found twice
                        fInd.pop()
                        fInd.pop()
                else:
                    fInd.append(occ[1]+1)
            else:
                fInd.pop()
            print('Potential solution', v, 'at', i , ' with Found ',money-v , ' at ', occ, '\t fInd: ' , fInd)
            if len(fInd)==2:
                print(fInd[0], fInd[1])      
                return
    return
'''

def whatFlavors(cost, money): #using dictionary 
    ind = {}
    for i, v in enumerate(cost):
        if v in ind.keys():
            ind[v].append(i)
        else:
            ind[v]=[i]
    print(ind)

    for i in range(len(cost)):
        if money - cost[i] in ind.keys():
            if len(ind[money-cost[i]])==2:
                print(i+1, ind[money- cost[i]][1]+1)
                return
            elif len(ind[money-cost[i]])==1 and not money-cost[i]==cost[i]: #case with complimentary int present and  complimentary int in not the number itself
                print(i+1, ind[money- cost[i]][0]+1)
                return
        

    return
money = 4

cost = '1 4 5 3 2'
#cost = '2 2 4 3'
#money = 8
#cost = '4 3 2 5 7'

#money =5
#cost = '1 2 3 5 6'
cost = list(map(int, cost.split()))
whatFlavors(cost, money)
