def rollhash(string):
    p=31
    m = 10**9+9
    charsum =0
    
    for ch in range(len(string)):
        charsum+=(ord(string[ch])-ord('A'))*(p**ch)
    val = charsum%m
    return val

def matchingStringsv2(strings, queries):
    #calculates hash only when needed (encounters a new string)
    occ = []
    hashes = []
    dict1 ={}
    saw = []
    for s in strings:
        if s in saw:
            continue
        else:
            shash = rollhash(s)
            hashes.append(shash)
            if shash in dict1.keys():
                #print(s," is NOT new string")
                dict1[shash]+=1
            else:
                #print(s," is new string")
                dict1[shash]=1
    print("Hashes array :", hashes)
    print("Dictionary :", dict1 )
    for q in queries:
        qhash = rollhash(q) 
        if (qhash in dict1.keys()):
            #print(dict1[qhash])
            occ.append(dict1[qhash])
        else:
            occ.append(0)
    return occ    

#further optimation, prepopulate the values of p**n in an array till max(len(string))
#maybe calculate hashes only for queries
def matchingStrings(strings, queries):
    occ = []
    hashes = []
    dict1 ={}
    for s in strings:
        shash = rollhash(s)
        hashes.append(shash)
        if shash in dict1.keys():
            #print(s," is NOT new string")
            dict1[shash]+=1
        else:
            #print(s," is new string")
            dict1[shash]=1
    #print("Hashes array :", hashes)
    #print("Dictionary :", dict1 )
    for q in queries:
        qhash = rollhash(q) 
        if (qhash in dict1.keys()):
            #print(dict1[qhash])
            occ.append(dict1[qhash])
        else:
            occ.append(0)
    return occ 
'''
n = 4
st = ['aba' , 'baba','aba','xzxb'] 
q = 3
qu = ['aba', 'xzxb', 'ab']
'''
n = 13
st= ['abcde', 'sdaklfj' , 'asdjf', 'na' , 'basdn' , 'sdaklfj', 'asdjf' , 'na' , 'asdjf' , 'na' , 'basdn' , 'sdaklfj' , 'asdjf']
q = 5
qu = ['abcde' , 'sdaklfj' , 'asdjf' , 'na', 'basdn']
print(matchingStringsv2(st, qu))