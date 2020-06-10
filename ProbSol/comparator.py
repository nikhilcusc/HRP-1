'''
https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
'''
class Player:
    def __init__(self, name, score):
        self.AllSubjList=[] 
    def __repr__(self):
        
    def comparator(a, b):

def divQS(arr, low, high):
    if high>low:
        pi = divQuickSortInP(arr, low, high)
        divQS(arr, low, pi-1)
        divQS(arr, pi+1, high)
    return arr
def divQuickSortInP(arr, low, high): #inplace
    #pivot index
    pi=low
    pivot = arr[pi]
    for i in range(pi+1,high+1):
        if arr[i]<=pivot:
            temp=arr[i]
            for i1 in range(i,pi,-1):
                arr[i1] = arr[i1-1]
            arr[pi] = temp
            #print(temp, arr, pi)
            pi+=1
    print(arr)
    return pi

l1 =['4 5 3 7 2 4']
nlist = list(map(int, l1[0].split()))

print(divQS(nlist, 0, len(nlist)-1))

def comparator(a,b):
    #if a<b, -1
    # a==b, 0
    # a>b, 1
    #equal scores
    '''
    if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
    '''
    if a.score==b.score: 
        #compare based on names
        aName, bName = b.name, b.name
        print(aName, bName)
        if len(aName)==len(bName):
            for i in range(len(aName)):
                if not aName[i]==bName[i]:
                    return 1 if aName[i]>bName[i] else -1
            return 0
        # the one with longer name is greater
        else:
            return 1 if len(aName)>len(bName) else -1
    else:
        return 1 if a.score>b.score else -1
    return 

s1 = ['david', 100]
s2 = ['david', 100]
print(comparator(s1,s2))