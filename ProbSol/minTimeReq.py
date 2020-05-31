'''
You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.
https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
'''

def minTime(machines, goal):
    def production(machines, days):
        prod = 0
        for i in machines:
            prod+=(mid)//i
        return prod

    minTime = int( (goal/len(machines) )*(min(machines)))
    maxTime = int( (goal/len(machines) )*(max(machines)))
    
    
    while  minTime<maxTime:
        
        mid = (minTime + maxTime)//2
        prod = production(machines, mid)
        print(mid, prod, goal,abs(prod-goal))
        if prod>=goal:
            maxTime = mid
        else:
            minTime = mid+1
    print('min, max',minTime, maxTime, 'abs(prod-goal)',abs(prod-goal))
    
    return minTime

t=  12
a = '4 5 6'
#t = 10
#a = '1 3 4'
#t= 5
#a='2 3'
machines = list(map(int, a.split()))

print(minTime(machines, t))