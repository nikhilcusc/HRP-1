
import ProbSol.Tree.initiali as BT

k = [1,2,5,3,6,4]

Bt= BT.BinaryTree(k[0])
for _ in range(1,len(k)):
    Bt.addNode(Bt.root,k[_])

print("Inorder  ",Bt.inorder(Bt.root))
print("Preorder ",Bt.preorder(Bt.root))
print("Postorder ",Bt.postorder(Bt.root))


 