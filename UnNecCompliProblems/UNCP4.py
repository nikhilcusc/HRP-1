'''
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
'''
def LCM(x,y):
    # x and y should be positive
    if x>0 or y>0:
        greater=0 
        if x>y:
            greater = x
        elif x==y:
            return x
        else:
            greater = y
        while 1:
            if greater%x==0 and greater%y==0:
                return greater
            greater+=1
    return 0

def kangaroo(x1, v1, x2, v2):
    if (v1>v2 and x1>x2) or (v1<v2 and x1<x2):
        #1 kangaroo ahead for other and hopping faster, slower would never be able to catch
        return 'NO'
    else:
        #faster kangaroo behind the slower one
        iters = LCM(v1,v2)/v1
        print('iters', iters)
        iters=int(iters) + max(x1,x2)
        k1,k2=0,0
        for i in range(iters+1):
            k1 = x1+i*v1
            k2 = x2+i*v2
            print('At timepoint : ',i,' k1: ', k1, ' k2: ',k2)
            if k1==k2:
                return 'YES'
    return 'NO'


str1 = '0 3 4 2'
#x1, v1, x2, v2
str2 = '0 2 5 3'
arr = list(map(int, str1.split()))
print(kangaroo(arr[0],arr[1],arr[2],arr[3]))