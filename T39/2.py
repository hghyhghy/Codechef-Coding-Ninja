# Problem statement
# You are given a ‘Binary Tree’.



# Return the preorder traversal of the Binary Tree.



# Example:
# Input: Consider the following Binary Tree:

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def preorder_traversal(root):
    
    if root is None:
        
        return
    
    print(root.val)

    preorder_traversal(root.left)

    preorder_traversal(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorder_traversal(root))