def findPathBST(root,data):
    if root==None:
        return None
    if root.data==data:
        l=list()
        l.append(root.data)
        return l
    leftOutput=findPathBST(root.left,data)
    if leftOutput!=None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput=findPathBST(root.right,data)
    if rightOutput!=None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None