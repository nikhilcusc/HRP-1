
class BinaryTreeNode:
    def __init__(self,data):
        self.info = data
        self.left = None
        self.right = None
        return

class BinaryTree:
    def __init__(self,data):
        self.root=BinaryTreeNode(data)
    def addNode(self,parentNode,data):
        if parentNode.info<data :
            if parentNode.right:
                self.addNode(parentNode.right,data)
            else:
                #print('Adding',data,' right child to ',parentNode.info)
                parentNode.right = BinaryTreeNode(data)
        else:
            if parentNode.left:
                self.addNode(parentNode.left,data)
            else:
                #print('Adding ',data,' left child to ',parentNode.info)
                parentNode.left = BinaryTreeNode(data)
    def inorder(self,parentNode):
        if parentNode:
            self.inorder(parentNode.left)
            print(parentNode.info, end=' ')
            self.inorder(parentNode.right)
        return
    def preorder(self,parentNode):
        if parentNode:
            print(parentNode.info, end=' ')
            self.preorder(parentNode.left)
            self.preorder(parentNode.right)
        return
    def postorder(self,parentNode):
        if parentNode:
            self.postorder(parentNode.left)
            self.postorder(parentNode.right)
            print(parentNode.info, end=' ')
        return