# check wheather a tree is BST

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def is_bst(root,min_val=float("-inf"),max_val=float("inf")):

    if not root:
        
        return True
    
    if not (min_val < root.val < max_val):

        return False
    
    
    return(is_bst(root.left,min_val,root.val) and is_bst(root.right,root.val,max_val))



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(11)
root.right.right = TreeNode(20)

print(is_bst(root))
        
        
    
    
    
    