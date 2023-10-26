class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.numNodes=0
    def printTree(self):
        return
    def isPresent(self,data):
        return False
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
