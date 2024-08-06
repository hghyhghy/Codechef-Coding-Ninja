# preorder traversal 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right=right
        
def preorder_traversal(root):
    
    if root is not None:
        
        print(root.val , end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(preorder_traversal(root))