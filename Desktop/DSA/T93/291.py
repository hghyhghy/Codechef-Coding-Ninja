

#postorder 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def preorder(root):
    
    if not root:
        
        return None
    
    if root:
        print(root.val)
        
        preorder(root.left)

        preorder(root.right)


    
if __name__ == "__main__":
    # Example tree: 
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    # Get the postorder traversal
    result = preorder(root)
    
    # Print the result
    print(result)