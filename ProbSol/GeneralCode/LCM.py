def LCM(x,y):
    # x and y should be positive
    if x>0 or y>0:
        greater=0 
        if x>y:
            greater = x
        elif x==y:
            return x
        else:
            greater = y
        while 1:
            if greater%x==0 and greater%y==0:
                return greater
            greater+=1
    return 0

checkList = [[12,15],[13,17],[51,17],[2,6],[1024,24],[1024,2],[11,13]]
for x in checkList:
    print(x,':',LCM(x[0],x[1]))