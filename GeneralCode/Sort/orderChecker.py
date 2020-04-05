def orderChecker(ReturnedList):
    for i in range(len(ReturnedList)-1):
        if ReturnedList[i]>ReturnedList[i+1]:
            return False
    return True