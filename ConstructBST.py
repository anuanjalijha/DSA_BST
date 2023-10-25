class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def convert(arr, start, end):

    # Base case.
    if (start > end):
        return None
    else:

        # Find 'mid' index of array and make it root node.
        mid = (start + end) // 2
        rootNode = BinaryTreeNode(arr[mid])

        # Call 'convert' function for the left part of array to make leftSubtree of root node.
        rootNode.left = convert(arr, start, mid - 1)

        # Call 'convert' function for the right part of array to make rightSubtree of root node.
        rootNode.right = convert(arr, mid + 1, end)

        # Return the rootNode.
        return rootNode


def constructBST(lst):
    n = len(lst)
    root = convert(lst, 0, n - 1)
    return root
    
        
