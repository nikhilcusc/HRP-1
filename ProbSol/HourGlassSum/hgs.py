def hg(arr,i,j):
    neighbours = [[-1,-1],[-1,0],[-1,1],[0,0],[1,-1],[1,0],[1,1]]
    s=0
    for neighbour in neighbours:
        #print("in hg ",i+neighbour[0],j+neighbour[1])
        s+=arr[i+neighbour[0]][j+neighbour[1]]
    return s

def hgsmax(arr):
    n = len(arr) #square matrix
    hgsums=[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            hgsums.append(hg(arr,i,j))
    print("all sum hour glasses",hgsums)
    return max(hgsums)
    

arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]]

print(hgsmax(arr))