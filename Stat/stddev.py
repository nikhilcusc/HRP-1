def mean(arr):
    return sum(arr)/len(arr)

def standdev(n, arr):
    marr = mean(arr)
    fluc = []
    for i in arr:
        fluc.append((i-marr)**2)

    return (sum(fluc)/n)**(1/2)

n=5
arr=[10,40,30,50,20]

print(format(standdev(n,arr),'.1f'))