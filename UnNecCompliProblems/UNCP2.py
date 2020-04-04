'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
'''

def countingValleys(n,s):
    topo=[]
    toposum=0
    for step in s:
        if step=='U':
            toposum+=1
        elif step=='D':
            toposum-=1
        topo.append(toposum)
    print("topo : ",topo)
    v=0
    for i in range(1,len(topo)):
        if topo[i-1]==-1 and topo[i]==0:
            v+=1
    return v

def countingValleys2(n,s): #reduce the space complexity
    # topo=[] Do not really need this
    toposum=0
    topoprev=0
    v=0
    
    for step in s:
        topoprev=toposum
        if step=='U':
            toposum+=1
        elif step=='D':
            toposum-=1
        
        if topoprev==-1 and toposum==0:
            v+=1
    return v


s= 'UDDDUDUU'
#s = 'DDUUUDDDUDUU'
V = countingValleys2(len(s),s)
print(V)