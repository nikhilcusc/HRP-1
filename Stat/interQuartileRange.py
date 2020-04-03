# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(arr):
    print(arr)
    if len(arr)%2:
        return arr[int(len(arr)/2)]
    else:
        return (arr[int(len(arr)/2)]+arr[int(len(arr)/2)-1])/2

def quartiles(n,arr):
    quar=[]
    if n%2:
        quar.append(median(arr[0:int(n/2)]))
        quar.append(arr[int(n/2)])
        quar.append(median(arr[int(n/2)+1:n]))

    else:
        
        quar.append(median(arr[0:int(n/2)]))
        quar.append(median(arr))
        quar.append(median(arr[int(n/2):n]))
    return quar

n=6
ele = [6,12,8,10,20,16]
freq = [5,4,3,2,1,5]

arr=[]
for i in range(len(ele)):
    arr.append([ele[i]]*freq[i])
print(arr)
art = [i for j in arr for i in j]
print("art",art)
art.sort()

qu= quartiles(len(art),art)
for i in qu:
    print(int(i))

print(format(qu[2]-qu[0],'.1f'))

