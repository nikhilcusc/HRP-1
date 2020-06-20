'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''

def isValid(s):
    maxf, minf =0, 9999
    freqDic = {}

    for c in s:
        if c in freqDic.keys():
            freqDic[c]+=1
        else:
            freqDic[c]=1
    print('FreqDic:',freqDic, freqDic.values(), min(freqDic.values()))    
    
    minf, maxf = min(freqDic.values()), max(freqDic.values())
    print ('minF and maxF',minf, maxf)
    if maxf-minf==1:
        count=[0 for _ in range(maxf)]
        for f in freqDic.values():
            count[f-1]+=1 #account for python indexing  
        print('Case with frequencies differ by 1',count)
        count = count[minf-1:]
        print(count)
        if count[0]==1 or count[1]==1:
            return 'YES'
    elif maxf==minf:
        return 'YES'
    elif minf==1 and len(set(list(freqDic.values())))==2: #1 extra character that can be removed
        counter=0
        print('case with minf==1')
        for f in freqDic.values():
            if f==1:
                counter+=1
        print('counter', counter)
        if counter==1:
            return 'YES'
    return 'NO'

s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'

print(isValid(s))