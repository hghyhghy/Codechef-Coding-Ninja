

class TreeNode:

    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right


def is_leaf(root):

    return  root is not None and root.left is None and root.right is None

def main(root):

    if not root:

        return  0

    total = 0

    if root.right and is_leaf(root.right):

        total += root.right.val

    total += main(root.left)


    total += main(root.right)

    return  total

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(main(root))
