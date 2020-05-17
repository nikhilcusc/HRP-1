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

def reverse_bisect_left(sequence, x, lower_bound=0, higher_bound=None):
    """Return the index where to insert item x in list a, assuming a is sorted in reverse.
    """
    if lower_bound < 0:
        raise ValueError("lo must be non-negative")
    if higher_bound is None:
        higher_bound = len(sequence)
    while lower_bound < higher_bound:
        middle = (lower_bound + higher_bound) // 2
        if sequence[middle] > x:
            lower_bound = middle + 1
        else:
            higher_bound = middle
    return lower_bound, higher_bound


def leaderboard_rank(scores, score, higher_bound=None):
        result, previous_higher_bound = reverse_bisect_left(scores, int(score), higher_bound=higher_bound)
        return result + 1, previous_higher_bound


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
    previous_higher_bound = len(rankScores)
    ranks = []
    for ascore in alice:
        result, previous_higher_bound = leaderboard_rank(rankScores, ascore, previous_higher_bound)
        ranks.append(result)
    return ranks


'''
scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
'''
scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

print(scores, '\n', [i for i in range(len(scores))])
print(climbingLeaderboard(scores, alice))