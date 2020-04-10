'''
ilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
'''

def repeatedString(s, n):
    counter=0
    for i in s:
        if i=='a':
            counter+=1
    counter*=(n//len(s))
    i=0
    while i<n%len(s):
        if s[i]=='a':
            counter+=1
        i+=1
    return counter

s='a'
n=10

print('a is repeated ',repeatedString(s, n),' times')