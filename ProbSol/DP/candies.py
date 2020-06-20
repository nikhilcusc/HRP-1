'''
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.
'''

def candies(n, arr):
    c = [1 for i in range(n)]

    if arr[0]>arr[1]:
        c[0]=2

    for i in range(1,len(arr)):
        #print(arr[i],arr[i-1],arr[i]>arr[i-1])
        if arr[i]>arr[i-1]:
            c[i]=c[i-1]+1
    print('First pass: ',c)

    for i in reversed(range(len(arr)-1)):
        print(i,arr[i],arr[i-1],arr[i]>arr[i-1])
        if arr[i]>arr[i+1]:
            c[i]=max(c[i+1]+1,c[i])
    print('Second pass: ',c)

    return sum(c)

n,arr =10, [2,4,2,6,1,7,10,9,2,1]
#n,arr =3, [1,2,2]
print(candies(n, arr))
