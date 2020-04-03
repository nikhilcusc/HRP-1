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
def probBino(n,x,p):
    ''' print("\n calFactorial(",n,") : ", calFactorial(n))
    print("\n calFactorial(",n-x,") : ", calFactorial(n-x))
    print("\n calFactorial(",x,") : ", calFactorial(x))
    '''
    
    comb = (calFactorial(n))/(calFactorial(n-x)*calFactorial(x))
    prob = comb*(p**x)*((1-p)**(n-x))
    return prob
def probBinoCummlative(n,x,p):
    CummaltiveProb = 0
    for iter1 in range(x,n+1):
        #print("probBino(",n,",",iter1,",",p,"): \t",probBino(n,iter1,p))
        CummaltiveProb+= probBino(n,iter1,p)
    return CummaltiveProb

arr = [0.88,0.12] #[success rate, failure rate]
p = arr[0]/sum(arr)
q= 1-p
#print("\n p : ",p,"\t q :",q)
n =10 # number of pistons
x=2
print(format(1-probBinoCummlative(n,3,q),'.3f')) # atmost 2 defective
print(format(probBinoCummlative(n,x,q),'.8f')) # atleast 2 defective
