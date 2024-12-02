
#validate bst 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def main(node,low=float("-inf"),high=float("inf")):
    
    if not node:
        
        return True
    
    if node.val <=low or node.val >=high:
        
        return False
    
    low=main(node.left,low,node.val)
    high=main(node.right,node.val,high)
    
    return low,high


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

# Check if the tree is a BST
if main(root):
    print("The tree is a BST.")
else:
    print("The tree is NOT a BST.")
    