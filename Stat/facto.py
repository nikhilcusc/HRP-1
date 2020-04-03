import sys

val = 1
def factorial(x):
    global val
    if x==1:
        return val
    val *=x 
    return factorial((x-1))

j =sys.argv
print(factorial(j))