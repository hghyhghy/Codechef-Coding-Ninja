# You have been given a binary tree of integers with N number of nodes. Your task is to check if that input tree is a BST (Binary Search Tree) or not.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def check_valid(node,low=float("-inf"),high=float("inf")):
    
    if not node:
        
        return True
    
    if node.val<=low  or node.val>=high:
        
        return False
    
    left=check_valid(node.left,low,node.val)
    right=check_valid(node.right,node.val,high)

    return left and right


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

# Check if the tree is a BST
if check_valid(root):
    print("The tree is a BST.")
else:
    print("The tree is NOT a BST.")
    
    
        
        