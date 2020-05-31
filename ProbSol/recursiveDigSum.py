def getDigitSum(n):
    digitSum=0
    while n>1:
        #print(n, digitSum)
        digitSum += n%10
        n//=10
    return digitSum + n

def superDigit(n, k):
    ds = getDigitSum(n)
    start = ds*k
    print('Starting with : ', start)
    while start>9:
        start = getDigitSum(start)
        print('Got: ',start)
    return start  

n = 9875
k = 4
superDigit(n, k)