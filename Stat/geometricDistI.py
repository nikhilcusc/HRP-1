def GeometericProb(insp,sp):

    return sp**(insp-1)*(1-sp)

#inp1 = list(map(int,input()))

n,d=1,3
sp = 1-n/d #probability of being not defective
print(sp)
insp = 5

print(GeometericProb(insp,sp))# prob1

#prob2 during first 5 inspections
totalProb=0
for i in range(1,insp+1):
    print("GeometericProb(",i,",sp)", GeometericProb(i,sp))
    totalProb+=GeometericProb(i,sp)
print(totalProb)