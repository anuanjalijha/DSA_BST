class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.numNodes=0
    def printTreeHelper(self,root):
        if root==None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print("L",root.left.data,end=",")
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
    def printTree(self):
        self.printTreeHelper(self.root)
    def isPresentHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            #call on left
            return self.isPresentHelper(root.left,data)
        else:
            #Call on right
            return self.isPresentHelper(root.right,data)
    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)
    def insert(self,data):
        return
    def deleteData(self):
        return False
    def count(self):
        return 0

b=BST()
b.insert(10)
b.insert(5)
b.insert(12)
print(b.isPresent(10))
print(b.isPresent(7))
print(b.isPresent(4))
print(b.isPresent(10))
print(b.count())
b.printTree()