def invertDict(dict1):
    invdict = {}
    for k,v in dict1.items():
        if v in invdict.keys():
            invdict[v].append(k)
        else:
            invdict[v]=[k]
    return invdict
    

d = {1: 2, 2: 2, 3: 1, 5: 3, 8: 1, 9: 1, 6: 1, 7: 1}
print(invertDict(d))