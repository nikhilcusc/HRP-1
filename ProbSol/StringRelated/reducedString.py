'''
Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String
'''

def superReducedString(s):
    
    def nonAdajecentChecker(k):
        for i in range(1,len(k)):
            if k[i]==k[i-1]:
                return True
        return False
    nonAj = nonAdajecentChecker(s)
    '''
    while nonAj:
        ns = ''
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                ns = s[i+1:]
                s = ns
                print(ns)
                continue
    '''
    def reduceString(s):
        ns=''
        for i in range(1,len(s),2): 
            if not s[i]==s[i-1]: #this needs update by 1
                ns+=s[i-1:i+1]
            #print(i, ns, s[i-1:i+1])
        
        if len(s)-i==2:
            ns+=s[-1]
        return ns
    while nonAj:
        s = reduceString(s)
        print('Returned String: ', s)
        nonAj = nonAdajecentChecker(s)
    if len(s)==0:
        return 'Empty String'
    return s
k = 'baab'
print(superReducedString(k))