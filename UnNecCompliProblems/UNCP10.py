'''
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i..j] and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where i-reverse(i) is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.
'''

def revser(i):
    c = str(i)
    revNum = ''
    for c1  in reversed(c):
        revNum+=(c1)
    #print(revNum, int(revNum))
    return int(revNum)
def beautifulDays(i, j, k):
    counter =0
    for i in range(i,j+1):
        #print('Checking ', i)
        if (abs(i - revser(i))%k) == 0:
            counter+=1
        
    return counter

i = 20
j=23
k=6

print(beautifulDays(i,j,k))