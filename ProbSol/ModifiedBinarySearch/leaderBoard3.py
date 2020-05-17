'''
Implementation of modified binary search using iterations instead of recursion
'''
def binSearchMod(list1, value, start, end): #implemented for descending order
    while end-start >1: 
        mid = (start + end)//2
        if list1[mid] == value:
            return True, mid
        if list1[mid] < value:
            end = mid
        else:
            start = mid 
    return False, start
    

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

    ranks = []
    for ascore in alice:
        if ascore<scores[len(scores)-1]: # alice scores are smaller than all
            res.append(len(set(scores))+1)
        elif ascore > scores[0]: #alice score is greatest
            res.append(1)
        else: #alice score lies somewhere in between
            present, Ind = binSearchMod(rankScores, ascore, 0 , len(rankScores)-1)
            print(ascore, present)
            if present:
                res.append(Ind+1) # to account for 1-indexed array
            else:
                res.append(Ind+2)
    return res


'''
scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
'''
scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

print(scores, '\n', [i for i in range(len(scores))])
print(climbingLeaderboard(scores, alice))