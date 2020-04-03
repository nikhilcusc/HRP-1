import ProbSol.Tree.initiali as BT

def tV(root):
    pass
    return

k = [1,6,7,12,8,9,11]
k = [1,2,5,3,6,4]

Bt= BT.BinaryTree(k[0])
for _ in range(1,len(k)):
    Bt.addNode(Bt.root,k[_])

print(Bt.root)

