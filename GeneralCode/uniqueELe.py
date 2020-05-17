def getUniqueEle(a):
    noDup = []
    for i in a:
        if not i in noDup:
            noDup.append(i)
    return noDup