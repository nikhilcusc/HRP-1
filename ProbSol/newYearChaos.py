'''
t's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

'''
def minimumBribes(q):
    moves =0
    q = [p-1 for p in q]
    print(q)
    for i, p in enumerate(q):
    
        if p-i>2:
            print('Too chaotic')
            return
        print('at: ', i, '\t looking between ', range(max(0,p-1),i))
        for j in range(max(0,p-1),i):
            print(' Checking : ', q[j],' > ',p )
            if q[j]>p:
                moves+=1
        print('\n\n')
    print(moves)
    return
'''
def minimumBribes(q):
    print(q)
    start = [i for i in range(1,len(q)+1)]
    diffArray = []
    for i in range(len(q)):
        change = q[i] - start[i]
        if change>=3:
            print('Too chaotic')
            return
        diffArray.append(change)
    print(diffArray)
    bribes, i =0, 0
    while i < len(diffArray):
        print('At i:', i, ' with bribes: ',bribes)
        if diffArray[i] ==1:
            bribes+=1
        elif diffArray[i]==2:
            bribes+=2
        i+=1
    print(bribes)
    return bribes
'''
q = '1 2 5 3 7 8 6 4'
#q= '2 5 1 3 4'
qw = list(map(int, q.split()))
print(minimumBribes(qw))