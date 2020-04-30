'''
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i]:

L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].
T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.
'''
# only finds k largest elements instead of sorting the whole list
#O(kn)?
def luckBalance(l, contests):
    Luck=[[],[]] #at 0 non imp contest, at 1 imp contest
    for contest in contests:
        Luck[contest[1]].append(contest[0])
    print("Luck : ",Luck)
    maxArr = [] 
    minEle=99999
    for _ in range(k):
        if len(maxArr):
            minEle = min(maxArr)
        tempMaxEle=0
        for i in Luck[1]:
            if i > tempMaxEle and  i < minEle:# does not allow duplicates
                tempMaxEle=i
        maxArr.append(tempMaxEle)
    print('Max arr',maxArr)

    minArr=[]
    for i in Luck[1]:
        if i not in maxArr:
            minArr.append(i)
    print('Min arr',minArr)

    TotalLuck=sum(Luck[0]) + sum(maxArr) - sum(minArr)
    return TotalLuck
'''
# need a faster solution than this
def luckBalance(k, contests):
    Luck=[[],[]] #at 0 non imp contest, at 1 imp contest
    for contest in contests:
        Luck[contest[1]].append(contest[0])
    #print("Luck : ",Luck)
    Luck[1].sort(reverse=1)
    #print(Luck)
    TotalLuck = sum(Luck[0])
    for i in range(k):
        TotalLuck+=Luck[1][i]
    for i in range(k,len(Luck[1])):
        TotalLuck-=Luck[1][i]
    return TotalLuck
'''
'''
k =2
contest=[[5,1],[1,1],[4,0]]

'''
k=3
contest=[[5,1],[2,1],[1,1],[8,1],[10,0],[5,0],[5,1]]

print(luckBalance(k, contest))
