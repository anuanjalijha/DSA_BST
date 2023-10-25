class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elementsInRangeK1K2(root, k1, k2):
    if root == None:
        return
    if root.data > k1:
        elementsInRangeK1K2(root.left, k1, k2)
    
    # If the current node's data is within the range [k1, k2], print it
    if k1 <= root.data <= k2:
        print(root.data, end=" ")
    
    # Traverse the right subtree if the current node's data is less than k2
    if root.data < k2:
        elementsInRangeK1K2(root.right, k1, k2)
