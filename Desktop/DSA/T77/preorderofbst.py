# You have been given an array/list 'PREORDER' representing the preorder traversal of a BST with 'N' nodes. All the elements in the given array have distinct values.

# Your task is to construct a binary search tree that matches the given preorder traversal.

# A binary search tree (BST) is a binary tree data structure that has the following properties:

# • The left subtree of a node contains only nodes with data less than the node’s data.
# • The right subtree of a node contains only nodes with data greater than the node’s data.
# • Both the left and right subtrees must also be binary search trees.
# Note:

# It is guaranteed that a BST can be always constructed from the given preorder traversal. Hence, the answer will always exist.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def preorder(root):
    
    if root is None:
        
        return None
    
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