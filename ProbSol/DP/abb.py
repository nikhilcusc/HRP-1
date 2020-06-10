'''
https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

'''

'''
def abbreviation(a, b):
    def compareChars(c1,c2):
        val=False
        if ord(c1)-32 == ord(c2):
            val=True
        return val

    while len(a) and len(b):
        #last characters match, regardless of uppercase
        if a[-1]==b[-1] or compareChars(a[-1],b[-1]):
            #trim the last character in both stings
            print('Matching character found: ', a[-1], b[-1])
            a=a[:-1]
            b=b[:-1]
        #else remove a char only from 'a'
        else:
            if ord(a[-1])<96:
                return False
            print('Trimming last character form a',a[-1])
            a=a[:-1]
        print('a,b:',a,b)
    # Check for any uppercase character remaining 'a' string
    for i in a:
        if ord(i)<96:
            return False
    #could not empty the 'b' string
    if len(b)>0:
        return False
    return True
'''
def abbreviation(a,b):
    d=[[0 for _ in range(len(b)+1)] for i in  range(len(a)+1)]
    
    d[0][0]=1
    for i in range(len(a)):
        for j in  range(len(b)+1):
            #skip the row if previous is 0
            if d[i][j]==0:
                continue
            # character matches then move to next character for both strings and make it 1
            if j<len(b) and a[i].upper() == b[j]:
                d[i+1][j+1]=1
            # if charater does not match and in string 'a' character is lower, we can remove it hence we can keep it 1, as it is possible to match the 2 stings
            if not a[i].isupper():
                d[i+1][j]=1

    if d[len(a)][len(b)]:
        return 'YES'
    return 'NO'

a = 'AbCdE'
b= 'AFE'


print(abbreviation(a, b))

'''
10
XXVVnDEFYgYeMXzWINQYHAQKKOZEYgSRCzLZAmUYGUGILjMDET
XXVVDEFYYMXWINQYHAQKKOZEYSRCLZAUYGUGILMDETQVWU
PVJSNVBDXABZYYGIGFYDICWTFUEJMDXADhqcbzva
PVJSNVBDXABZYYGIGFYDICWTFUEJMDXAD
QOTLYiFECLAGIEWRQMWPSMWIOQSEBEOAuhuvo
QOTLYFECLAGIEWRQMWPSMWIOQSEBEOA
DRFNLZZVHLPZWIupjwdmqafmgkg
DRFNLZZVHLPZWI
SLIHGCUOXOPQYUNEPSYVDaEZKNEYZJUHFXUIL
SLIHCUOXOPQYNPSYVDEZKEZJUHFXUIHMGFP
RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGGnscruaa
RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGG
AVECtLVOXKPHIViTZViLKZCZAXZUZRYZDSTIHuCKNykdduywb
AVECLVOXKPHIVTZVLKZCZAXZUZRYZDSTIHCKN
wZPRSZwGIMUAKONSVAUBUgSVPBWRSTJZECxMTQXXA
ZPRSZGIMUAKONSVAUBUSVPBWRSTJZECMTQXXA
SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFYyxu
SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFY
EIZGAWWDCSJBBZPBYVNKRDEWVZnSSWZIw
EIZGAWWDCSJBBZPBYVNKRDEWVZSSWZI
NO
YES
YES
YES
NO
YES
YES
YES
YES
YES
'''