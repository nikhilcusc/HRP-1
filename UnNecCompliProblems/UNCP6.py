'''
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month m and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

'''

def birthday(s, d, m):
    counter,i=0,0
    
    for i in range(m,len(s)+1):
        print(i-m,i,s[i-m:i])
        if sum(s[i-m:i]) == d:
            counter+=1
    return counter

s= '1 1 1 1 1 1'
s='1 2 1 3 2'
s='4'
d,m = 4, 1

s= list(map(int,s.split()))

print("she can divide the chocolate in ", birthday(s, d, m), " ways.")