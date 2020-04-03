import math
val = 1
def calFactorial (b):
    global val
    val = 1
    def factorial(x):
        global val
        if x<=0:
            return 1
        if x==1:
            return val
        val *=x 
        return factorial((x-1))
    return factorial(b)
def probpoi(p,q):
    ''' print("\n calFactorial(",n,") : ", calFactorial(n))
    print("\n calFactorial(",n-x,") : ", calFactorial(n-x))
    print("\n calFactorial(",x,") : ", calFactorial(x))
    '''
    prob = (p**q)*(math.e)**(-p)
   
    return prob/calFactorial(q)
'''
def probpoiCummlative(n,x,p):
    CummaltiveProb = 0
    for iter1 in range(x,n+1):
        #print("probBino(",n,",",iter1,",",p,"): \t",probBino(n,iter1,p))
        CummaltiveProb+= probBino(n,iter1,p)
    return CummaltiveProb
'''
days=1
p = 0.88
q= 1.55
print("\n p : ",p,"\t q :",q)

print(format(probpoi(p,days),'.8f'))
print(format(probpoi(q,days),'.8f'))