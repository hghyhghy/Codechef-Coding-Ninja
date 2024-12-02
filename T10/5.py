# post order traversal 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def post_order(root):
    
    if root is not None:
        
        post_order(root.left)
        post_order(root.right)
        print(root.val ,end=" ")

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(post_order(root))