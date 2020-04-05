'''
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
'''
import ProbSol.GeneralCode.LCM as LCM1
def getTotalX(a, b):
    X=0
    #a.sort() 
    #b.sort() #O(nlogn)  used sorting just to find min element
    bmax = max(b)
    #LCM of arr1:
    LCM=1
    if len(a):
        LCM=a[0]
    else:
        for i in range(1,len(a)):
            l =  LCM1.LCM(a[i-1],a[i])
            LCM = max(l,LCM)
    print('Chosen base element : ',LCM)
    ele = LCM
    intlist=[]
    counter, flag=1,1
    while ele<bmax: # change this later
        ele = LCM * counter
        counter+=1
        flag=1
        for a2 in b:
            print('flag: ',flag,'\t a2:',a2,'\t ele:',ele,'\t a2%ele:',a2%ele )
            if a2%ele:
                flag=0
        if flag:
            intlist.append(ele)
    print(intlist)
    X=len(intlist)
    return X
#str1='2 4'
str1='2'
str2 = '20 30 12'

arr1 = list(map(int, str1.split()))
arr2 = list(map(int, str2.split()))

print(getTotalX(arr1, arr2))