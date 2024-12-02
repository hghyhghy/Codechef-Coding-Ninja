

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def main(root):
    
    if not root:
        
        return None
    
    current=root
    
    while current and current.right:
        
        current=current.right
        
    return current.val 


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print(main(root))