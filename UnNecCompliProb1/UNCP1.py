def solve(N,arr):
    seq = [[] for x in range(N)]
    lastA = 0
    for ele in arr:
        print("\n Ele : ", ele, "\tseq : ",seq)
        dec = ele[0]
        if dec==1:
            seqop = (ele[1]^lastA)%N
            seq[seqop].append(ele[2])
        elif dec==2:
            seqop = (ele[1]^lastA)%N
            lastA = seq[seqop][ele[2]%(len(seq[seqop]))] #super complicated 
            # the question desciption does not explain this properly
            print(lastA)
    return

arr = [[1, 0, 5],
[1, 1, 7],
[1, 0, 3],
[2, 1, 0,],
[2, 1, 1,],
]

N=2
Q=5


print(solve(N,arr))