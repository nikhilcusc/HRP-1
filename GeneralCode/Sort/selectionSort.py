def Sort(a):
    n = len(a)
    s=0
    while s<n:
        minv=9999
        i=s
        #find the min value in unsorted array
        while i <n:
            if a[i]<minv:
                minv=a[i]
                minInd = i #save the index
            i+=1
        #swap the value at index i with first value in unsorted array
        temp = a[minInd]
        a[minInd] = a[s]
        a[s] = temp 
        s+=1
    return a
