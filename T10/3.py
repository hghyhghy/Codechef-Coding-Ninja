# inorder traversal 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def inorder_traversal(root):
    
    if root is not  None:
        
        inorder_traversal(root.left)
        print(root.val , end=" ")
        inorder_traversal(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(inorder_traversal(root))