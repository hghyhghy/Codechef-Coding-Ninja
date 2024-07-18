# find the minimum element from the binary search tree 

class TreeNode:

    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right


def return_minimum(root):

    current = root

    while current.left is not None:

        current=current.left

    return current.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

result = return_minimum(root)
print("The minimum element from the binary tree is ", result)