'''
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print the number of times the client will receive a notification over all n days.
'''
## does not execute within time limits!
def findMedian(a):
    n = len(a)
    s=0
    while s<(n/2)+1:
        minv=9999
        i=s
        #find the min value in unsorted array
        while i <n:
            if a[i]<minv:
                minv=a[i]
                minInd = i #save the index
            i+=1
        #swap the value at index i with first value in unsorted array
        temp = a[minInd]
        a[minInd] = a[s]
        a[s] = temp 
        s+=1
    print(a)
    if len(a)%2:
        return a[int(len(a)/2)]
    return (a[int(len(a)/2)] + a[int(len(a)/2)-1])/2

def activityNotifications(expenditure, d):
    NotCounter=0
    for i in range(d,len(expenditure)):
        med = findMedian(expenditure[i-d:i])
        print(i, expenditure[i-d:i], med, expenditure[i])
        if 2*med<=expenditure[i]:
            NotCounter+=1
    return NotCounter
#n,d=5,4
#exp= '1 2 3 4 4'
n,d = 9, 6
exp = '2 3 4 2 3 6 8 4 5'
exp = list(map(int, exp.split()))
print('Number of notifications : ',activityNotifications(exp,d))