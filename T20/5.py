
# maximum element from the bst 

class TreeNode:

    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right


def maximum_element(root):

    current = root 

    while current.right is not None:

        current=current.right

    return current.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

result=  maximum_element(root)
print("Maximum element", result)