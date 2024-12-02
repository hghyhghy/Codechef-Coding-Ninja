

#minimum in bst 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def main(root):
    
    if not root:
        
        return 0
    
    curr =root
    
    while curr.left is not None:
        
        curr=curr.left
        
    return curr.val

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

print(main(root))