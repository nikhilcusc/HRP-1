def simpleOrderChecker(ReturnedList):
    for i in range(len(ReturnedList)-1):
        if ReturnedList[i]>ReturnedList[i+1]:
            return False
    return True

def exactOrderChecker(ReturnedArray, unsortedArray):
    sortedArray = unsortedArray.copy()
    sortedArray.sort()
    
    if ReturnedArray==sortedArray:
        return True
    return False
