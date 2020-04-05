import GeneralCode.Sort.bubbleSort as B

import random
import os
from datetime import datetime, timedelta
import GeneralCode.Sort.orderChecker as OC


print('Running GeneralCode.Sort.list which has multiple lists')

l1 =['3 2 1 4','64 59 876 263 31 9 87 10 926 628 804 598538 972 507 576',
'429 146 331 415 424',
'0 880 474 93 310',
'-617 -639 -28 538 -490 -246 983',
'960 928 961 908 981 934 934',
'89 92 93 96 93 90 98 90 89 94 95 90 91 98 90 94 94',
'-35 -78 186 312 583 774 754 640 564 -10 2 852 62 7 817 18 778 535 888 651 726 373 766 160 357 202 643 101 831 261 295 195 -42 -45 574 471 865 154 75 568 991 734 904 48 -63 923 976 250 995 157 275 523 406 266 82 609 286 -62']


for l in range(len(l1)):
    nlist = list(map(int, l1[l].split()))
    timeBefore = datetime.now()
    ###   
    ReturnedList = B.Sort(nlist)
    ###
    timeAfter = datetime.now()
    print('\n List number:',l,'\t Time taken: ',timeAfter-timeBefore,'\t Order Correct?', OC.orderChecker(ReturnedList),'\nOriginal List: ',l1[l],'\n Returned List:',ReturnedList,'\n')
