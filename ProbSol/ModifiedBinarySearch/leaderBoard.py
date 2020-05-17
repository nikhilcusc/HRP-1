'''
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking.
'''
#idea is to search for current score using binary search and return nearest index
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
    #conditions for out of range
    if value>list1[start] : 
        return [False ,start]
    if value<list1[end]:
        return [False, end]
    if value < list1[mid]:
        return binSearchMod(list1, value, mid, end)
    else:
        return binSearchMod(list1, value, start, mid)

def climbingLeaderboard(scores, alice): # O(log n)
    # all the edge cases 
    res=[]
    
    rank =1
    rankScores=[scores[0]] 
    #ssign ranks to scores
    for score in range(1,len(scores)):
        if scores[score]!=scores[score-1]:
            rank+=1
            rankScores.append(scores[score])
    print('Unique scores: ', rankScores)
    #go through each score to assign a rank
    for ascore in alice:
        if ascore>scores[len(scores)-1]:
            bsResult = binSearchMod(rankScores, ascore, 0 , len(rankScores)-1)
            print(ascore, bsResult)
            if bsResult[0]:
                res.append(bsResult[1]+1)
            else:
                res.append(bsResult[1]+2)
        else:
            res.append(len(set(scores))+1)
    return res
'''
def climbingLeaderboard(scores, alice): # try with something else, need a faster solution
    res=[]

    rank =1
    rankScores=[1]
    for score in range(1,len(scores)):
        if scores[score]!=scores[score-1]:
            rank+=1
        rankScores.append(rank)
    print('Scores: ',scores, '\nranks: ',rankScores)
    for ascore in alice:
        rankAssigned=False
        for ind in range(len(scores)):
            if ascore  >= scores[ind] and not rankAssigned:
                res.append(rankScores[ind])
                rankAssigned=True
        if not rankAssigned:
            res.append(rank+1)
    return res
'''

scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
'''
scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]
'''
print(scores, '\n', [i for i in range(len(scores))])
print(climbingLeaderboard(scores, alice))