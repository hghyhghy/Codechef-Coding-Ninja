# Problem statement
# You are given a ‘Binary Tree’.



# Return the preorder traversal of the Binary Tree.

class BinaryTreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def preorder(root):
    
    if not root:
        
        return []
    
    if root:
        
        print(root.val)
        
        preorder(root.left)

        preorder(root.right)
        

root = BinaryTreeNode(1)           # Root node
root.left = BinaryTreeNode(2)      # Left child of root
root.right = BinaryTreeNode(3)     # Right child of root

root.left.left = BinaryTreeNode(5) # Left child of node 2
root.right.left = BinaryTreeNode(6) # Left child of node 3
root.right.right = BinaryTreeNode(7) # Right child of node 3

# Output preorder traversal
print("\nPreorder Traversal of the tree is: ")
preorder(root)