# smallest in the BST 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def check_smallest(node):
    
    if node is None:
        
        return None
    
    current = node
    while current.left is not None:
        
        current=current.left
        
    return current.val

root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(check_smallest(root))