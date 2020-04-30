'''
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1.

'''

def pickingNumbers(a):
    # Write your code here
    
    #print(a)
    arrD = {i:0 for i in range(0,max(a)+1)}
    #print(arrD)
    for i in a:
            arrD[i]+=1
    longestConLen, maxlCL, anchor=0, 0, arrD[0]
    #print( arrD)
    for k in arrD.keys():
        if arrD[k]:
            print(k, arrD[k])
    
    for k in range(1,max(a)+1):
        if arrD[k-1] and arrD[k]  :
            longestConLen = arrD[k] + arrD[k-1]
        else:
            longestConLen=0
            anchor=k
        if maxlCL<longestConLen:
            maxlCL = longestConLen
    if maxlCL==0 or maxlCL<max(arrD.values()):
        maxlCL=max(arrD.values())
    return maxlCL

l1 =['3 20 1 24','1 -3 71 68 17','64 59 876 263 31 9 87 10 926 628 804 598538 972 507 576',
'429 146 331 415 424',
'0 880 474 93 310',
'-617 -639 -28 538 -490 -246 983',
'960 928 961 908 981 934 934',
'89 92 93 96 93 90 98 90 89 94 95 90 91 98 90 94 94',
'-35 -78 186 312 583 774 754 640 564 -10 2 852 62 7 817 18 778 535 888 651 726 373 766 160 357 202 643 101 831 261 295 195 -42 -45 574 471 865 154 75 568 991 734 904 48 -63 923 976 250 995 157 275 523 406 266 82 609 286 -62']

l1 =['4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97']

for l in range(len(l1)):
    nlist = list(map(int, l1[l].split()))
    ###   
    ReturnedInt = pickingNumbers(nlist)
    ###
    print(ReturnedInt)
    