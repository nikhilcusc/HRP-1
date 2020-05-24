'''

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?
'''

def makeAnagram(a, b):
    aDic={}
    bDic={}
    for c in a:
        if c in aDic.keys():
            aDic[c]+=1
        else:
            aDic[c]=1
    for c in b:
        if c in bDic.keys():
            bDic[c]+=1
        else:
            bDic[c]=1
    print('aDic', aDic, '\t bDic:',bDic)
    count=0
    for c in aDic.keys():
        if c in bDic.keys():
            bDic[c] = abs(aDic[c] - bDic[c])
        else:
            count += aDic[c]
    print('aDic', aDic, '\t bDic:',bDic)
    
    for c in bDic.keys():
        count += bDic[c]
    return count

a = 'cde'
b = 'dcf'
print(makeAnagram(a, b))