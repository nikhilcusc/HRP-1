'''
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
'''
#method 1
def push(arr,x):
    arr.insert(0,x)
    return arr

def pop(arr):
    arr.pop(0)
    return arr

def maxArr(arr):
    return max(arr)

#method 2
#store the max while inserting in the stack, removes the need of O(n) operations while finding max


n = 10
inp= [[1, 97],[2],[1, 20],[2],[1,26],[1,20],[2],[3],[1,91],[3]]
arr=[]
for i in inp:
    print(i)
    if len(i)==2:
        push(arr,i[1])
    if i[0] ==2:
       arr= pop(arr)
    if i[0]==3:
        print(maxArr(arr))