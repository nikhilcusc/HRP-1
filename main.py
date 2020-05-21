import datetime
import itertools
from itertools import permutations
x = datetime.datetime.now()
print(x.strftime("%d-%b-%y\n\n"))

#import ProbSol.nonAdjSubsetSum

#import GeneralCode.ExceptionHandling.exception1
#import GeneralCode.Sort.lists
#import GeneralCode.permComb
#import Regex.MasterMatchstr
#import UnNecCompliProblems.UNCP11


val=1
def extraLongFactorials(n):
    if n==1:
        return val
    return n*extraLongFactorials(n-1)

print(extraLongFactorials(25))
