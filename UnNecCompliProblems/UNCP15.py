

k=3
arr = [4, 2, 6, 1, 10]
'''
pg=0
pgChap=[]
for a in arr:
    
    pgChap.append([ list(range(pg+1,pg+(((a-1)//k)+1)+1)) ])
    pg+=(((a-1)//k)+1)
    #print(a, (((a-1)//k)+1),pg)
print(pgChap)
'''

pgArr=[[]]
pgN = 0

for a in arr:
    probCounter=0
    pgArr.append([])
    pgN+=1
    for prob in range(1,a+1):
        print(pgArr, '\t adding: ', prob, 'with probCounter',probCounter)
        if probCounter<k:
            pgArr[pgN].append(prob)
            probCounter+=1
        else:
            probCounter=1
            pgArr.append([])
            pgN+=1
            pgArr[pgN].append(prob)
        
print(pgArr)
counter=0
for i,v in enumerate(pgArr):
    print('index: ', i , '\tValue:', v)
    if i in v:
        counter+=1

print(counter)