'''
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
'''
def appendStr(str1, c):
    str1+=c
    return str1

def appendAndDelete(s, t, k):
    while k>=0:
        if s==t:
            return 'YES'
        if s[:len(t)]!=t:
            t=t[:-1]
        else :
            t+=s[len(t)]

            
        k-=1
        print(t)
    return 'NO'

s= 'ashley'
t= 'ash'
k= 2
'''
s='hackerhappy'
t='hackerrank'
k=9
'''
print(appendAndDelete(s,t,k))