from datetime import datetime, timedelta 
import os
import GeneralCode.Sort.orderChecker as OC
##
import GeneralCode.Sort.selectionSort as B 
##

l1 =['3 2 1 4']
print('Running GeneralCode.Sort.list which has 1 list and orders in Ascending order')
nlist = list(map(int, l1[0].split()))
timeBefore = datetime.now()
ReturnedList = B.Sort(nlist)
timeAfter = datetime.now()
print('\nOriginal List: ',l1[0],'\n Returned List:',ReturnedList,'\n Time taken: ',timeAfter-timeBefore,'\t Order Correct?', OC.orderChecker(ReturnedList),'\n')
