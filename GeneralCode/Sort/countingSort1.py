#given the array will have values between 0 and 100

def Sort(arr):
    d1 = {key : 0 for key in range(min(arr),max(arr))}
    for i in arr:
        if i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
    #print(d1.keys())
    temparr=[]
    for key in d1.keys():
        if d1[key]:
            for i in range(d1[key]):
                temparr.append(key)
    #print(temparr)
    return temparr
'''
# below is from wiki
def Sort(a):
    k = max(a)
    count = [0]*(k+1)
    for x in a:
        count[x]+=1
    #print('Count :',count)
    total=0
    for i in range(k+1):
        count[i], total = total, count[i]+total
    #print('Count2 :',count)

    output = [0]*len(a)    
    for i in a:
        #print(output,i,count[i])
        output[count[i]]=i
        count[i]+=1
    return output
'''
'''
l1 =['1 1 1 7 2']
nlist = list(map(int, l1[0].split()))

print(Sort(nlist))
'''