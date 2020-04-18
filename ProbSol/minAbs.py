'''
Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
'''
from datetime import datetime
def minimumAbsoluteDifference(arr):
    minasb=99999
    diffarr = []
    arr.sort()
    for i in range(1,len(arr)):
        diffarr.append(abs(arr[i-1]-arr[i]))
    print(diffarr)

    return min(diffarr)


l1 =['3 20 1 24','1 -3 71 68 17','64 59 876 263 31 9 87 10 926 628 804 598538 972 507 576',
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
    ReturnedInt = minimumAbsoluteDifference(nlist)
    ###
    timeAfter = datetime.now()
    print('\n List number:',l,'\t Time taken: ',timeAfter-timeBefore,'\nOriginal List: ',l1[l],'\n Returned List:',ReturnedInt,'\n')
