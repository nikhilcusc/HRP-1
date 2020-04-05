
def Sort(a):
    swap=1
    passCounter=1
    while swap:
        swap=0
        for i in range(1,len(a)):
            if a[i-1]>a[i]:
                temp = a[i-1]
                a[i-1]=a[i]
                a[i]=temp
                swap+=1
        passCounter+=1
        #print('Arr: ',a, ' \t Swap value: ',swap,' \t Pass: ',passCounter)
    return a



