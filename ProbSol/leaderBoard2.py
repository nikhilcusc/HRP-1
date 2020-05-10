def binSearchMod(list1, value, start, end): #implemented for descending order
    mid = (start+end)//2
    #print('Looking for value: ', value, ' in ', start, end, mid , 'list :', list1)
    #conditions for element at start or end or mid
    if value == list1[start]:
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


def climbingLeaderboard(scores, alice): # O(log n), not really we have to go through all scores to determine their rank. This passes all cases except 1, if we can reduce get ranks instead of going through all list, maybe we can pass all cases
    res=[]
    rank =1
    rankScores=[scores[0]] 
    #assign ranks to scores
    for score in range(1,len(scores)):
        if scores[score]!=scores[score-1]:
            rank+=1
            rankScores.append(scores[score])
    print(rankScores)
    for ascore in alice:
        if ascore<scores[len(scores)-1]: # alice scores are smaller than all
            res.append(len(set(scores))+1)
        elif ascore > scores[0]: #alice score is greatest
            res.append(1)
        else: #alice score lies somewhere in between
            bsResult = binSearchMod(rankScores, ascore, 0 , len(rankScores)-1)
            print(ascore, bsResult)
            if bsResult[0]:
                res.append(bsResult[1]+1)
            else:
                res.append(bsResult[1]+2)
    return res


'''
scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
'''
scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

print(scores, '\n', [i for i in range(len(scores))])
print(climbingLeaderboard(scores, alice))