	
# Check if a tree is a BST or BT

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def check_bst(node,left=float('-inf'),right=float('inf')):
    
    if node is None:
        
        return True
    
    if not (left < node.val < right):
        
        return False
    
    return (check_bst(node.left,left,node.val) and check_bst(node.right ,node.val,right))



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(check_bst(root))
    
    