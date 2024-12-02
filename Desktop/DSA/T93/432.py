

#preorder of bst

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right



def preorder(root):

    if root is None:

        return  None

    print(root.val)
    preorder(root.left)
    preorder(root.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Perform preorder traversal
print("Preorder Traversal of the BST:")
preorder(root)