'''
Binary search implementation
returns index of element if present, otherwise returns False
'''
from itertools import permutations

def binSearch(list, value, start, end): #implemented for descending order
    mid = (start+end)//2
    #print(mid)
    if value>list[start] or value<list[end]:
        return False
    if value==list[start]:
        mid = start
    if value == list[end]:
        mid = end
    if value == list[mid]:
        return mid
    if value < list[mid]:
        return binSearch(list, value, mid, end)
    else:
        return binSearch(list, value, start, mid)

    return False

l1 =['3 2 1 4','64 59 876 263 31 9 87 10 926 628 804 598538 972 507 576',
'429 146 331 415 424',
'0 880 474 93 310',
'-617 -639 -28 538 -490 -246 983',
'960 928 961 908 981 934 934',
'89 92 93 96 93 90 98 90 89 94 95 90 91 98 90 94 94',
'-35 -78 186 312 583 774 754 640 564 -10 2 852 62 7 817 18 778 535 888 651 726 373 766 160 357 202 643 101 831 261 295 195 -42 -45 574 471 865 154 75 568 991 734 904 48 -63 923 976 250 995 157 275 523 406 266 82 609 286 -62']

l1 = list(permutations([i for i in range(4)]))
#print(l1, list(l1[0]))
'''
#i=l1[1]
#nlist = list(map(int, i.split()))
#nlist.sort(reverse=True)
#print(nlist,'\n', [i for i in range(len(nlist))])
#print(binSearch(nlist, 598538, 0, len(nlist)-1))
'''
for i in l1:
    #nlist = list(map(int, i.split()))
    nlist = list(i)
    nlist.sort(reverse=True)
    
    print(nlist,'\n', [i for i in range(len(nlist))])
    print(binSearch(nlist, 2, 0, len(nlist)-1),'\n\n')
