class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Solution
def searchInBST(root, k):
    if root==None:
        return False
    if root.data==k:
        return True 
    elif k>root.data:
        return searchInBST(root.right,k)
    else:
        return searchInBST(root.left,k)             

