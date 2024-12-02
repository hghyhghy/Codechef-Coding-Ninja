
class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def main(root):
    
    if root is None:
        
        return None
    
    curr=root
    while curr.left:
        
        curr=curr.left
        
    return curr.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print(main(root))