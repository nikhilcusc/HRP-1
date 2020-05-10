l1 = [1,2,4]

'''
try:
    print(l1[4])
except:
    print('Out of eange')
'''
dic1={}
for i in l1:
    dic1[i]=1

for i in range(5):
    try:
        print(i, dic1[i])
    except KeyError :
        print('Out of range')
        continue